"""Spoke Street Bike Repair: open repair slots."""


def bays_left(capacity, booked):
    """Return how many repair slots are still open."""
    return max(capacity - booked, 0)


def can_book(capacity, booked, bikes=1):
    """Return True when the booking fits in the open repair slots."""
    return bikes <= bays_left(capacity, booked)
