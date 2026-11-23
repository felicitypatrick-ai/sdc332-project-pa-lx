import unittest

from app.queue import queue_position


class LineTests(unittest.TestCase):
    def test_first_is_number_one(self):
        self.assertEqual(queue_position(["Patel", "Kim", "Lopez"], "Patel"), 1)

    def test_not_on_list_gets_zero(self):
        self.assertEqual(queue_position(["Patel", "Kim"], "Lopez"), 0)

    def test_third_is_number_three(self):
        self.assertEqual(queue_position(["Patel", "Kim", "Lopez"], "Lopez"), 3)
