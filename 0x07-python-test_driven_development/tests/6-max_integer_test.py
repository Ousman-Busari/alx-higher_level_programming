#!/usr/bin/python3
"""
Module to test the function use to find
the max integer in a list

"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A class with different test cases for max_integer function
    as methods

    """
    def test_zero_length(self):
        # Test the case where the length of the list is zero
        self.assertEqual(max_integer([]), None)

    def test_list_of_int_and_floats(self):
        # Test the case where all elements of a list are integers
        self.assertEqual(max_integer([4, 6, 3, 1, 7, 9, 8, 2]), 9)
        self.assertEqual(max_integer([4, 6, 3.8, 1.9, -5.6, 4.7, 8.5, 2]), 8.5)

    def test_max_at_begging(self):
        # Test the case where the max element is at the beginning of the list
        self.assertEqual(max_integer([14, 6, 3, 1, 7, 9, 8, 2]), 14)

    def test_max_at_end(self):
        # Test the case where the max element is at the end of the list
        self.assertEqual(max_integer([14, 6, 3, 1, 7, 9, 8, 22]), 22)

    def test_list_of_negatives(self):
        # Test the case where the max element is at the beginning
        self.assertEqual(max_integer([-14, -6, -3, -1, -7, -9]), -1)

    def test_list_of_int_and_floats(self):
        # Test the case where all elements of a list are integers
        self.assertEqual(max_integer([4, 6, 3, 1, 7, 9, 8, 2]), 9)
        self.assertEqual(max_integer([4, 6, 3.8, 1.9, -5.6, 4.7, 8.5, 2]), 8.5)

    def test_string_type(self):
        # Test case for an argument of non-list type
        self.assertEqual(max_integer("string"), 't')
