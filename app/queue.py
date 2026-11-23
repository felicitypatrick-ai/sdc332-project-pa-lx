"""Spoke Street Bike Repair: queue for full days."""


def queue_position(queue, customer):
    """Return the customer's place in line, or 0 when not on the queue."""
    if customer not in queue:
        return 0
    return queue.index(customer) + 1
