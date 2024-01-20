#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        Class to test MaxInteger
    """
    def test_simple(self):
        """
            test_simple for simple test cases on max
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([2, 4, 1]), 4)
        self.assertEqual(max_integer([-2, 2, 4, 3]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([21]), 21)

    def test_none(self):
        self.assertIsNone(max_integer([]))

    def test_error(self):
        """
            Test_error to test int instead of list
        """
        self.assertRaises(TypeError, max_integer, 21)
