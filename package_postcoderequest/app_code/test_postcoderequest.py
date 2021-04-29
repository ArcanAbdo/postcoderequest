from postcode_class import PostCode

import unittest
import pytest


class PostcodeTests(unittest.TestCase):

    # This postcode exists
    postcode_example1 = PostCode("B14 7EG")

    def test_1_check_length(self):
        self.assertEqual(self.postcode_example1.check_length(), "Postcode length is valid")

    def test_1_output_full(self):
        self.assertIs(self.postcode_example1.output_full(), dict)
