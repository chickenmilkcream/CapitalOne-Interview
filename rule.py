"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""
from collections import defaultdict
from typing import List, Tuple


class Rule:
    """
    A credit card system rule for rewarding points for transactions.

    Instance Attributes:
      - rule_id: the unique id of the rule
      - requirements: a dictionary mapping merchant_code to amount based on the specifications of the rule
          - merchant_code: the merchant to purchase from
          - amount: the amount the user have to spend
      - reward: the number of points rewarded for meeting the requirements of this rule

    Representation Invariants:
      - rule_id >= 1
      - reward >= 1
    """
    rule_id: int
    requirements: defaultdict[str, int]
    reward: int

    def __init__(self, rule_id: int, requirements: List[Tuple[str, int]], reward: int) -> None:
        self.rule_id = rule_id
        self.requirements = defaultdict(int)
        for merchant_code, amount in requirements:
            self.requirements[merchant_code] = amount
        self.reward = reward

    def __str__(self) -> str:
        return "Rule {rule_id} is added with the following requirements {requirements} and reward {reward}".format(
            rule_id=str(self.rule_id),
            requirements=str(dict(self.requirements)),
            reward=str(self.reward)
        )
