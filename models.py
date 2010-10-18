""" Models for use in PyOCR """

import parser

ZERO_STRING  = " _ | ||_|"
ONE_STRING   = "     |  |"
TWO_STRING   = " _  _||_ "
THREE_STRING = " _  _| _|"
FOUR_STRING  = "   |_|  |"
FIVE_STRING  = " _ |_  _|"
SIX_STRING   = " _ |_ |_|"
SEVEN_STRING = " _   _  _"
EIGHT_STRING = " _ |_||_|"
NINE_STRING  = " _ |_| _|"

ACCOUNT_STRING_TO_DIGIT_MAP = {
    ZERO_STRING  : 0,
    ONE_STRING   : 1,
    TWO_STRING   : 2,
    THREE_STRING : 3,
    FOUR_STRING  : 4,
    FIVE_STRING  : 5,
    SIX_STRING   : 6,
    SEVEN_STRING : 7,
    EIGHT_STRING : 8,
    NINE_STRING  : 9
}

class AccountManager:
    """ Manager for helping with Account string manipulation """
    def __init__(self, file):
        self.file = file
        self.accounts = self.get_accounts()
        self.account_numbers = self.get_account_numbers(self.accounts)

    def get_accounts(self):
        # return file as an iterator
        i = iter(self.file)
        # reads 4 lines at a time, join them into a string replacing the newlines
        return ( "".join((line1, i.next(), i.next(), i.next())).replace("\n", "") for line1 in i )

    def get_account_numbers(accounts):
        for account in accounts:
            digits = []
            # account here is the serialized string representation, each account string has 9 digits of 3 width
            # working with 3 lines here
            for i in range (0, parser.ACCOUNT_STRING_NUM_LINES):
                # chomp 3 chars from teh account string and put them in the digits spot
                for j in range (0, parser.ACCOUNT_DIGITS_COUNT):


        pass

class AccountNumber:
    """ Simple Class to model an Account Number """
    def __init__(self, digits=[]):
        # list of digits
        self.digits = digits

    @property
    def digits(self):
        return self.digits

    @property
    def numeric_repr(self):
        pass

    @property
    def string_repr(self):
        pass

class Digit:
    """ Simple Digit """
    def __init__(self, digit_string):
        # the raw digit represented as text including newline characters
        self.digit_string = digit_string

    @property
    def numerical_value(self):
        # returns the numerical value for this digit
        return ACCOUNT_STRING_TO_DIGIT_MAP[self._stripNewlines()]

    def _stripNewlines(self):
        # strips this digit of newlines
        return self.digit_string.replace(parser.NEWLINE_CHARACTER, parser.EMPTY_CHARACTER)


