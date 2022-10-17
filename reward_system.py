"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""
import constants
from math import floor
from typing import Dict, List
from rule import Rule


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
        print(f"Your current reward points total is: {self.total_points_rewarded}")

    def make_rules(self, rule_ids: List[int]) -> None:
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
        self.make_rules(rule_ids)

        for rule in self.rules:
            num_times_applied = self._apply_rule(rule.requirements)
            if num_times_applied:
                self.total_points_rewarded += (num_times_applied * rule.reward)
                self._print_rule_application_info("Rule " + str(rule.rule_id), num_times_applied, rule.reward)

        print("------------------------------------------------------------------------")
        print(f"Reward Calculation Finished.")
        print(f"Your reward points total is: {self.total_points_rewarded}")
