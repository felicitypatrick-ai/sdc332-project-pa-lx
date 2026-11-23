import unittest

from app.settings import DAILY_REPAIR_SLOTS


class SettingsTests(unittest.TestCase):
    def test_capacity_is_a_positive_number(self):
        self.assertGreater(DAILY_REPAIR_SLOTS, 0)
