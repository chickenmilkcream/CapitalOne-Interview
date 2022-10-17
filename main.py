"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: October 16th, 2022
"""
from reward_system import RewardsSystem
from transaction_system import TransactionSystem


def calculate_rewards() -> None:
    """
    Run the main reward points system and print the maximum points rewarded.
    """
    print("Welcome to the Credit Card Reward Points System :^) \n")
    input_path = input("Please enter the path of the transaction file (i.e. data/example_main.json): ")
    print("\n")

    transaction_system = TransactionSystem(input_path)
    total_per_merchant = transaction_system.get_total_per_merchant()
    reward_system = RewardsSystem(total_per_merchant)

    # Brute Force, apply rules in a greedy manner based on which rule gives the most points
    # Con: have to figure out redundant rules
    # rule_ids = [1, 2, 4, 6, 7]  # Got rid of rule 3 and 5 since applying rule 6 will give more points
    # reward_system.apply_all_rules_brute_force(rule_ids)

    # Optimized, use linear programming for scalability and efficiency
    rule_ids = [1, 2, 3, 4, 5, 6, 7]
    reward_system.apply_all_rules_optimized(rule_ids)


if __name__ == '__main__':
    calculate_rewards()
