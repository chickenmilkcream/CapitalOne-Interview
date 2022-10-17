"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""
import os.path
from datetime import datetime
from typing import List, DefaultDict
from transaction import Transaction
from collections import defaultdict
import json


class TransactionSystem:
    """
    A credit card transaction system.

    Instance Attributes:
      - transactions_list: the list of user credit card transactions

    Representation Invariants:
      - len(transactions_list) >= 0
    """
    transactions_list: List[Transaction]

    def __init__(self, transactions_path: str) -> None:
        self.transactions_list = self._import_data(transactions_path)

    def _import_data(self, transaction_path: str) -> List[Transaction]:
        """
        A private function that parses the transactions JSON file and return a list of Transaction objects.
        """
        if not os.path.isfile(transaction_path):
            print("Please restart and enter a valid file path.")
            exit(0)

        f = open(transaction_path)
        transactions = json.load(f)
        transactions_list = []

        date_time_format = '%Y-%m-%d'

        for transaction in transactions.values():
            # Transforms the string date format to a datetime object
            transaction["date"] = datetime.strptime(transaction["date"], date_time_format)
            # Converts cents to dollars
            transaction["amount"] = transaction["amount_cents"] / 100
            transactions_list.append(Transaction(transaction))

        f.close()

        return transactions_list

    def get_total_per_merchant(self) -> DefaultDict[str, float]:
        """
        Return a dictionary of the total amount spent per merchant.
        """
        total_per_merchant = defaultdict(int)
        for transaction in self.transactions_list:
            merchant = transaction.merchant_code
            amount = transaction.amount
            total_per_merchant[merchant] += amount

        return total_per_merchant
