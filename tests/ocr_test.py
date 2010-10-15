from unittest import TestCase
from pyocr import main

import logging

class IOTest(TestCase):

    def setUp(self):
        pass

    def test_main_raises_error_with_more_than_one_arg(self):
        self.assertRaises(TypeError, main, *["foo.txt", "bar"])

    def test_main_raises_error_when_file_is_not_found(self):
        self.assertRaises(IOError, main, [None, "badfile.txt"])

class ParseTest(TestCase):

    def setUp(self):
        self.ZERO_SERIALIZED = " _ | ||_|"  # base case with zero to start

    def test_parse_digit_returns_proper_value(self):
        import parser
        zero_unserialized = " _ \n| |\n|_|\n"
        parsed = parser.parse_digit(zero_unserialized)
        self.assertEquals(parsed, self.ZERO_SERIALIZED)
        
    def test_serialize_accounts_returns_list(self):
        import parser
        zero_one_unserialized = " _ \n| |\n|_|\n   \n  |\n  |\n"
        account_list = parser.parse_accounts(zero_one_unserialized)
        self.assertTrue(type(account_list) == list)

class OCRTest(TestCase):

    def test_sanity(self):
        self.assertTrue(True)

# Test Helpers

def _print(string):
    """ Simple helper to mock out the print function """
    return string

