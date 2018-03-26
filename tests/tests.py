import unittest

from tests.handler import test_send_message_handler


class SendMessageTest(unittest.TestCase):
    def test_bot_sends_proper_message(self):
        response = test_send_message_handler()
        self.assertEqual(response['statusCode'], 200)
