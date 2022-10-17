"""
Technical Assessment for Capital One

Candidate: Amy Peng
Date: February 4th, 2022
"""

SPORTCHECK = "sportcheck"
SUBWAY = "subway"
TIMHORTONS = "tim_hortons"
RULES = {
    "1": {
        "requirements": [
            (SPORTCHECK, 75),
            (TIMHORTONS, 25),
            (SUBWAY, 25),
        ],
        "reward": 500
    },
    "2": {
        "requirements": [
            (SPORTCHECK, 75),
            (TIMHORTONS, 25),
        ],
        "reward": 300
    },
    "3": {
        "requirements": [
            (SPORTCHECK, 75),
        ],
        "reward": 200
    },
    "4": {
        "requirements": [
            (SPORTCHECK, 25),
            (TIMHORTONS, 10),
            (SUBWAY, 10),
        ],
        "reward": 150
    },
    "5": {
        "requirements": [
            (SPORTCHECK, 25),
            (TIMHORTONS, 10),
        ],
        "reward": 75
    },
    "6": {
        "requirements": [
            (SPORTCHECK, 20),
        ],
        "reward": 75
    },
    "7": {
        "requirements": [
        ],
        "reward": 1
    }
}