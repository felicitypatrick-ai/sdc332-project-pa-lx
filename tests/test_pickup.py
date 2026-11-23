import unittest

from app.pickup import ready_message


class MessageTests(unittest.TestCase):
    def test_message_names_who_and_time(self):
        text = ready_message("Patel", "16:00")
        self.assertIn("Patel", text)
        self.assertIn("16:00", text)
