"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: October 16th, 2022
"""
from datetime import datetime


class Transaction:
    """
    A user credit card transaction.

    Instance Attributes:
      - date: the date of the transaction
      - merchant_code: the merchant the user purchased from
      - amount: the purchase amount in dollars of the transaction

    Representation Invariants:
      - amount >= 0
    """
    date: datetime
    merchant_code: str
    amount: int

    def __init__(self, transaction: dict) -> None:
        self.date = transaction["date"]
        self.merchant_code = transaction["merchant_code"]
        self.amount = transaction["amount"]

    def __str__(self) -> str:
        return "Transaction: {date} {merchant} {amount}".format(
            date=str(self.date),
            merchant=self.merchant_code,
            amount=str(self.amount)
        )
