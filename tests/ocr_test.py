from unittest import TestCase
from pyocr import main

ZERO_SERIALIZED = " _ | ||_|"
ZERO_UNSERIALIZED = " _ \n| |\n|_|\n"
ZERO_ONE_ACCOUNT_LIST = " _ \n| |\n|_|\n\n   \n  |\n  |\n\n"

class IOTest(TestCase):

    def setUp(self):
        pass

    def test_main_raises_error_with_more_than_one_arg(self):
        self.assertRaises(TypeError, main, *["foo.txt", "bar"])

    def test_main_raises_error_when_file_is_not_found(self):
        self.assertRaises(IOError, main, [None, "badfile.txt"])

class ParseTest(TestCase):

    def setUp(self):
        import parser
        self.parser = parser

    def test_parse_digit_returns_proper_value(self):
        parsed = self.parser.parse_digit(ZERO_UNSERIALIZED)
        self.assertEquals(parsed, ZERO_SERIALIZED)
        
    def test_parse_accounts_returns_list(self):
        account_list = self.parser.parse_accounts(ZERO_ONE_ACCOUNT_LIST)
        self.assertTrue(type(account_list) == list)

    def test_parse_accounts_raises_error_when_accounts_are_formatted_improperly(self):
        self.assertTrue(False)

class OCRTest(TestCase):

    def test_sanity(self):
        self.assertTrue(True)

# Test Helpers

def _print(string):
    """ Simple helper to mock out the print function """
    return string

