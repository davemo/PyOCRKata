""" Utilities to parse the account digits """

ACCOUNT_STRING_LINE_LENGTH = 27 # each line in an account string is 27 characters long
ACCOUNT_STRING_NUM_LINES = 3    # each account number is represented on 3 lines, the newline is stripped
RAW_DIGIT_WIDTH = 3             # digits are 3 characters wide
ACCOUNT_DIGITS_COUNT = 9        # each account number is made up of 9 digits
NEWLINE_CHARACTER = "\n"        # representation of the newline character in python
EMPTY_CHARACTER = ""