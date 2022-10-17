"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: October 16th, 2022
"""
import unittest
from reward_system import RewardsSystem
from transaction_system import TransactionSystem

rule_ids = [1, 2, 4, 6, 7]
full_rule_ids = [1, 2, 3, 4, 5, 6, 7]


class TestEmptyExample(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_empty.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules_brute_force(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_brute_force(rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 0)

    def test_apply_all_rules_optimized(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_optimized(full_rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 0)


class TestRule7(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_rule7.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules_brute_force(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_brute_force(full_rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 86)

    def test_apply_all_rules_optimized(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_optimized(full_rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 86)


class TestExample4(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_4.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    def test_apply_all_rules_brute_force(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_brute_force(rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 95)

    def test_apply_all_rules_optimized(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_optimized(full_rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 95)


class TestMainExample(unittest.TestCase):
    def setUp(self) -> None:
        transaction_system = TransactionSystem("data/example_main.json")
        total_per_merchant = transaction_system.get_total_per_merchant()
        self.reward_system = RewardsSystem(total_per_merchant)

    # Note to self: brute force is wrong because optimized found a better solution haha
    # def test_apply_all_rules_brute_force(self) -> None:
    #     """
    #     Test that it can sum a list of integers
    #     """
    #     self.reward_system.apply_all_rules_brute_force(rule_ids)
    #     total_points_rewarded = self.reward_system.total_points_rewarded
    #     self.assertEqual(total_points_rewarded, 1657)

    def test_apply_all_rules_optimized(self) -> None:
        """
        Test that it can sum a list of integers
        """
        self.reward_system.apply_all_rules_optimized(full_rule_ids)
        total_points_rewarded = self.reward_system.total_points_rewarded
        self.assertEqual(total_points_rewarded, 1662)


if __name__ == '__main__':
    unittest.main()
