#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """ This test the flowwing methonds.

    """

    def test_values(self):
        """ This test the values.

        """

        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([5, 3, 4, 2]), 5)
        self.assertAlmostEqual(max_integer([5, 3, -4, 2]), 5)
        self.assertAlmostEqual(max_integer([-5, -3, -4, -2]), -2)
        self.assertAlmostEqual(max_integer([5]), 5)
        self.assertAlmostEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
