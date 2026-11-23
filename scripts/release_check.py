"""Release check: run after each deploy with the deployed folder (course starter app)."""
import os
import sys

release, environment = sys.argv[1], sys.argv[2]
sys.path.insert(0, release)  # import the deployed files, not the repository's

from settings import DAILY_REPAIR_SLOTS
from bays import bays_left
from queue import queue_position

print(f"Release check: {environment}")
print(open(os.path.join(release, "BUILD_INFO.txt")).read().strip())
print("Repair slots per day:", DAILY_REPAIR_SLOTS)
print("Open repair slots with 18 booked:", bays_left(DAILY_REPAIR_SLOTS, 18))
print("Place in line of the first on the queue:", queue_position(["Patel", "Kim"], "Patel"))
print("Release check finished.")
