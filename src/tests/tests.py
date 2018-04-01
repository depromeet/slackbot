import unittest

from src.tests.handler import test_send_message_handler
from src.utils import parse_command, trigger_link


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


class TriggerLinkTest(unittest.TestCase):
    @unittest.skip('Function not yet implemented')
    def test_triggers_link_properly(self):
        sample_command = 'ㅎㅇ'
        link = trigger_link(sample_command)
        self.assertEqual(link, 'hi/')

    @unittest.skip('Test not yet implemented')
    def test_throws_error_when_command_not_found(self):
        sample_command = 'ㅗ'
        self.assertRaises(KeyError, sample_command)


if __name__ == '__main__':
    unittest.main()
