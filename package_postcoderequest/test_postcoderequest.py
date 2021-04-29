# Kieran
from taking_postcode import post_code_query

# Edward
from postcode_request_info import post_code_info

import unittest
import pytest


class PostcodeTests(unittest.TestCase):

    input_example = post_code_query()
    output_example = post_code_info()

    def test_example1(self):
        self.assertEqual(self.input_example.example1("", ""), "")

    def test_example2(self):
        self.assertEqual(self.output_example.example2("", ""), "")
