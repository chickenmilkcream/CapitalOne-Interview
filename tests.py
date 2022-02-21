"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""
import unittest
from reward_system import RewardsSystem
from transaction_system import TransactionSystem


class TestEmptyExample(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_empty.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules()
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 0)


class TestRule7(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_rule7.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules()
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 86)

class TestExample4(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_4.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules()
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 95)


class TestMainExample(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_main.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules()
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 1657)


if __name__ == '__main__':
    unittest.main()
