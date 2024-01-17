import unittest
from circles import circle
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle(1), pi)
        self.assertAlmostEqual(circle(0), 0)
        self.assertAlmostEqual(circle(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure vallue errors are raised
        self.assertRaises(ValueError, circle, -2)

    def test_types(self):
        # Make sure types errors are raised when necessary
        self.assertRaises(TypeError, circle, 3+5j)
        self.assertRaises(TypeError, circle, True)
        self.assertRaises(TypeError, circle, "Yo")
