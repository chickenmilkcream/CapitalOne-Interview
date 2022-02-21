"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""
import constants
from math import floor
from typing import Dict


class RewardsSystem:
    """
    A reward calculation system.

    Instance Attributes:
      - total_per_merchant: the dictionary of total amount spent per merchant
      - total_points_rewarded: the total points rewarded to the user per month

    Representation Invariants:
      - all(total > 0 for total in total_per_merchant.values())
      - total_points_rewarded >= 0
    """
    total_per_merchant: Dict[str, float]
    total_points_rewarded: int

    def __init__(self, total_per_merchant: Dict[str, float]) -> None:
        self.total_per_merchant = total_per_merchant
        self.total_points_rewarded = 0

    def _apply_rule(self, spending_required: Dict[str, float]) -> int:
        """
        Apply a rule given the requirements and return the number of times it was applied.
        """
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

    def apply_rule1(self) -> None:
        """
        Rule 1: 500 points for every $75 spend at Sport Check, $25 spend at Tim Hortons and $25 spend at Subway
        """
        spending_required = {
            constants.SPORTCHECK: 75,
            constants.TIMHORTONS: 25,
            constants.SUBWAY: 25,
        }
        points_rewarded_per_application = 500
        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 1", num_times_applied, points_rewarded_per_application)

    def apply_rule2(self) -> None:
        """
        Rule 2: 300 points for every $75 spend at Sport Check and $25 spend at Tim Hortons
        """
        spending_required = {
            constants.SPORTCHECK: 75,
            constants.TIMHORTONS: 25,
        }
        points_rewarded_per_application = 300

        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 2", num_times_applied, points_rewarded_per_application)

    def apply_rule3(self) -> None:
        """
        Rule 3: 200 points for every $75 spend at Sport Check
        """
        spending_required = {
            constants.SPORTCHECK: 75,
        }
        points_rewarded_per_application = 200

        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 3", num_times_applied, points_rewarded_per_application)

    def apply_rule4(self) -> None:
        """
        Rule 4: 150 points for every $25 spend at Sport Check, $10 spend at Tim Hortons and $10 spend at Subway
        """
        spending_required = {
            constants.SPORTCHECK: 25,
            constants.TIMHORTONS: 10,
            constants.SUBWAY: 10,
        }
        points_rewarded_per_application = 150

        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 4", num_times_applied, points_rewarded_per_application)

    def apply_rule5(self) -> None:
        """
        Rule 5: 75 points for every $25 spend at Sport Check and $10 spend at Tim Hortons
        """
        spending_required = {
            constants.SPORTCHECK: 25,
            constants.TIMHORTONS: 10,
        }
        points_rewarded_per_application = 75

        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 5", num_times_applied, points_rewarded_per_application)

    def apply_rule6(self) -> None:
        """
        Rule 6: 75 point for every $20 spend at Sport Check
        """
        spending_required = {
            constants.SPORTCHECK: 20,
        }
        points_rewarded_per_application = 75

        num_times_applied = self._apply_rule(spending_required)
        if num_times_applied:
            self.total_points_rewarded += (num_times_applied * points_rewarded_per_application)
            self._print_rule_application_info("Rule 6", num_times_applied, points_rewarded_per_application)

    def apply_rule7(self) -> None:
        """
        Rule 7: 1 points for every $1 spend for all other purchases (including leftover amount)
        """
        points_rewarded_per_application = 1
        num_times_applied = floor(sum(self.total_per_merchant.values()))
        if num_times_applied:
            self.total_points_rewarded += num_times_applied
            self._print_rule_application_info("Rule 7", num_times_applied, points_rewarded_per_application)

CREDIT_CARD_TO_RULES = {
    "Capital One 100": [1, 3, 5],
    "Capital One normal": [1, 3]
}

RULES_TO_POINTS = {
    1: 100,
    3: 300,
    5: 500,
}

RULES_TO_CONDITIONS = {
    1 : {
        constants.SPORTCHECK: 25,
        constants.TIMHORTONS: 10,
    }
}
    def apply_all_rules(self, credit_card) -> None:
        """
        Apply all the rules, in descending potential points awarded order.
        """
        list_of_rules = CREDIT_CARD_TO_RULES[credit_card]
        list_of_rules.sort()

        for rule in list_of_rules:
            self.apply_rule(rule, )

        # self.apply_rule1()
        # self.apply_rule2()
        # self.apply_rule3()
        # self.apply_rule4()
        # self.apply_rule5()
        # self.apply_rule6() # Got rid of rule 3 and 5 since applying rule 6 will give more points
        # self.apply_rule7()
        print("------------------------------------------------------------------------")
        print(f"Reward Calculation Finished.")
        print(f"Your reward points total is: {self.total_points_rewarded}")
