from unittest import TestCase
from pyocr import main

class IOTest(TestCase):

    def test_sanity(self):
        self.assertTrue(True)

    def test_main_raises_error_with_more_than_one_arg(self):
        self.assertRaises(TypeError, main, *["foo.txt", "bar"])

    def test_main_raises_error_when_file_is_not_found(self):
        self.assertRaises(IOError, main, ["badfile.txt"])

class OCRTest(TestCase):

    def test_sanity(self):
        self.assertTrue(True)