import unittest

from src.tests.handler import test_send_message_handler
from src.utils import parse_command


class SendMessageTest(unittest.TestCase):
    def test_bot_sends_proper_message(self):
        response = test_send_message_handler()
        self.assertEqual(response['statusCode'], 200)


class ParseCommandTest(unittest.TestCase):
    def test_parses_command_without_extra_space(self):
        sample_input = '<@U9UFVQKLZ>ㅎㅇ'
        parsed = parse_command(sample_input)
        self.assertEqual(parsed, 'ㅎㅇ')

    def test_parses_command_with_extra_space(self):
        sample_input = '<@U9UFVQKLZ> ㅎㅇ'
        parsed = parse_command(sample_input)
        self.assertEqual(parsed, 'ㅎㅇ')
