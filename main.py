"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
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
    reward_system.apply_all_rules()


if __name__ == '__main__':
    calculate_rewards()
