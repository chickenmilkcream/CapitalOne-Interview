"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: October 16th, 2022
"""
import constants
from math import floor
from typing import Dict, List
from rule import Rule
from ortools.linear_solver import pywraplp
from collections import defaultdict


class RewardsSystem:
    """
    A reward calculation system.

    Instance Attributes:
      - total_per_merchant: the dictionary of total amount spent per merchant
      - total_points_rewarded: the total points rewarded to the user per month
      - rules: the rules of this reward system

    Representation Invariants:
      - all(total > 0 for total in total_per_merchant.values())
      - total_points_rewarded >= 0
    """
    total_per_merchant: Dict[str, float]
    total_points_rewarded: int
    rules: List[Rule]

    def __init__(self, total_per_merchant: Dict[str, float]) -> None:
        self.total_per_merchant = total_per_merchant
        self.total_points_rewarded = 0
        self.rules = []

    def _apply_rule(self, spending_required: Dict[str, float]) -> int:
        """
        Apply a rule given the requirements and return the number of times it was applied.
        """
        # A special case for rule 7
        if len(spending_required) == 0:
            return floor(sum(self.total_per_merchant.values()))

        merchants = spending_required.keys()

        # Check if the merchants the user purchased from applies to this rule
        if not all(merchant in self.total_per_merchant for merchant in merchants):
            return 0

        # Check if the user spending amount from each merchant meets the minimum limit
        if not all(self.total_per_merchant[merchant] >= spending_required[merchant]
                   for merchant in merchants):
            return 0

        # Check how many times we can apply this rule
        num_times_applied = 0

        while all(self.total_per_merchant[merchant] - spending_required[merchant] >= 0
                  for merchant in merchants):

            # Subtract the appropriate amount per merchant after applying this rule once
            for merchant in merchants:
                self.total_per_merchant[merchant] -= spending_required[merchant]

            num_times_applied += 1

        # Return the total points awarded after applying this rule (could be multiple times)
        return num_times_applied

    def _print_rule_application_info(self, rule_name: str, num_times_applied: int,
                                     points_rewarded_per_application: int) -> None:
        print("------------------------------------------------------------------------")
        print(f"Applying {rule_name}: rewarded {points_rewarded_per_application} points per application")
        print(f"You've applied this rule {num_times_applied} times "
              f"and earned {num_times_applied * points_rewarded_per_application} points.")
        # print(f"Your current reward points total is: {self.total_points_rewarded}")

    def make_rules(self, rule_ids: List[int]) -> None:
        """
        Create Rule objects based on given rule IDs.
        """
        for rule in rule_ids:
            if str(rule) not in constants.RULES:
                print(str(rule) + " is not a defined rule. Please restart and enter a valid set of rules.")
                exit(0)
            self.rules.append(Rule(rule, constants.RULES[str(rule)]["requirements"], constants.RULES[str(rule)]["reward"]))

        for rule in self.rules:
            print(rule)

    def apply_all_rules_brute_force(self, rule_ids: List[int]) -> None:
        """
        Apply all the rules, in descending potential points awarded order.
        """
        print("------------------------------------------------------------------------")
        print(f"Added the following Rules to the System.")
        self.make_rules(rule_ids)

        for rule in self.rules:
            num_times_applied = self._apply_rule(rule.requirements)
            if num_times_applied:
                self.total_points_rewarded += (num_times_applied * rule.reward)
                self._print_rule_application_info("Rule " + str(rule.rule_id), num_times_applied, rule.reward)

        print("------------------------------------------------------------------------")
        print(f"Reward Calculation Finished.")
        print(f"Your reward points total is: {self.total_points_rewarded}")

    def apply_all_rules_optimized(self, rule_ids: List[int]) -> None:
        """
        Apply all the rules, in using linear programming.
        Following this article:
        https://mlabonne.github.io/blog/linearoptimization/
        https://mlabonne.github.io/blog/integerprogramming/

        KEY ASSUMPTION: Rule 7 is applied after optimizing for Rules 1-6
        """
        print("------------------------------------------------------------------------")
        print(f"Added the following Rules to the System.")

        self.make_rules(rule_ids[::-1])

        # Pop out Rule 7 because it's not part of the optimization
        rule7 = self.rules[0]
        del(self.rules[0])

        solver = pywraplp.Solver('Maximize Reward Points', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

        # Creating variables for Rules 1-6
        rule_vars = defaultdict()
        for rule in self.rules:
            rule_vars[rule.rule_id] = solver.IntVar(0, solver.infinity(), str(rule.rule_id))

        # Creating equations for each merchant
        # Each equation will look like this
        # sportcheck_eqn: 75 * rule1 + 75 * rule2 + 75 * rule3 + 25 * rule4 + 25 * rule5 + 20 * rule6
        # timhortons_eqn: 25 * rule1 + 25 * rule2 + 10 * rule4 + 10 * rule5
        # subway_eqn: 25 * rule1 + 10 * rule4

        sportcheck = self.total_per_merchant[constants.SPORTCHECK]
        timhortons = self.total_per_merchant[constants.TIMHORTONS]
        subway = self.total_per_merchant[constants.SUBWAY]

        merchant_eqn = defaultdict(int)
        for rule in self.rules:
            for merchant in rule.requirements.keys():
                if merchant in [constants.SPORTCHECK, constants.TIMHORTONS, constants.SUBWAY]:
                    merchant_eqn[merchant] += (rule.requirements[merchant] * rule_vars[rule.rule_id])

        solver.Add(merchant_eqn[constants.SPORTCHECK] <= sportcheck)
        solver.Add(merchant_eqn[constants.TIMHORTONS] <= timhortons)
        solver.Add(merchant_eqn[constants.SUBWAY] <= subway)

        # Creating the overall optimization equation for points
        # The optimization equation will look like this
        # optimize_eqn: rule1 * 500 + rule2 * 300 + rule3 * 200 + rule4 * 150 + rule5 * 75 + rule6 * 75

        optimize_eqn = 0

        for rule in self.rules:
            optimize_eqn += (rule.reward * rule_vars[rule.rule_id])

        solver.Maximize(optimize_eqn)
        optimal = solver.Solve()

        # Retrieving the number of times each rule was applied
        num_times_applied = defaultdict()
        for rule in self.rules:
            num_times_applied[rule.rule_id] = rule_vars[rule.rule_id].solution_value()

        # Update total_per_merchant to calculate for Rule 7
        for rule in self.rules:
            for merchant in rule.requirements.keys():
                self.total_per_merchant[merchant] -= (num_times_applied[rule.rule_id] * rule.requirements[merchant])

        # Update total_points_rewarded
        num_times_applied[rule7.rule_id] = floor(sum(self.total_per_merchant.values()))
        self.total_points_rewarded = solver.Objective().Value() + floor(sum(self.total_per_merchant.values()))

        # Printing everything out
        if optimal == pywraplp.Solver.OPTIMAL:
            print('An optimal solution was found for Rules 1-6')
        else:
            print('There is no optimal solution for Rules 1-6, only Rule 7 is applied')
        self.rules = self.rules[::-1]
        self.rules.append(rule7)
        for rule in self.rules:
            self._print_rule_application_info(str(rule.rule_id), num_times_applied[rule.rule_id], rule.reward)

        print("------------------------------------------------------------------------")
        print(f"Reward Calculation Finished.")
        print(f"Your reward points total is: {self.total_points_rewarded}")
