""" Main script for PyOCRKata """

import sys
import logging

def main(argv):

    if len(argv) > 2:
        raise TypeError("pyocr only takes 1 argument, usage: pyocr.py [filename]")

    filename = argv[1]

    try:
        file = open(filename)
    except IOError:
        raise IOError("Error opening file %s" % filename)

if __name__ == "__main__":

    main(sys.argv)

