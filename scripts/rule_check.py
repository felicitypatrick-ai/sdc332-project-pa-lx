"""Owner's rule checks (course starter app). Run: python scripts/rule_check.py capacity|limit|line|all"""
import os
import sys
import time

sys.path.insert(0, "app")
WAIT = 11  # seconds; stands in for a slow check of the live sign-up page


def capacity():
    time.sleep(WAIT)
    from settings import DAILY_REPAIR_SLOTS
    assert DAILY_REPAIR_SLOTS == 20, f"capacity is {DAILY_REPAIR_SLOTS}; the owner's rule says 20"
    print("capacity: OK")


def limit():
    time.sleep(WAIT)
    from bays import can_book
    assert not can_book(100, 0, bikes=3 + 1), "a booking bigger than the limit was accepted; the owner's rule says 3"
    print("limit: OK")


def line():
    time.sleep(WAIT)
    print(open(os.path.join("dist", "BUILD_INFO.txt")).read().strip())
    from queue import queue_position
    assert queue_position(["Patel", "Kim"], "Patel") == 1, "the first on the queue is not number 1"
    print("place in line: OK")


CHECKS = {"capacity": capacity, "limit": limit, "line": line}

for name in (CHECKS if sys.argv[1:] == ["all"] else sys.argv[1:]):
    CHECKS[name]()
