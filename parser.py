""" Utilities to parse the account digits """

ACCOUNT_STRING_LINE_LENGTH = 27 # each line in an account string is 27 characters long
ACCOUNT_STRING_NUM_LINES = 4    # each account number is represented on 4 lines, 3data + 1newline
RAW_DIGIT_WIDTH = 3             # digits are 3 characters wide

def parse_digit(account_string):
    # given an account string across multiple lines
    # strip the newline characters for this account string
    account_string = account_string.replace("\n", "")
    return account_string

def parse_accounts(accounts_string):
    # given a large string of accounts
    pass





