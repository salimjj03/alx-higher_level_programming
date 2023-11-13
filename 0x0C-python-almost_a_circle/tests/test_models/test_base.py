#!/usr/bin/python3
"""

The test models.

"""


import unittest
from models.base import Base


class testbase(unittest.TestCase):
    """ This test the base modulea.

    """

    def test_base(self):
        """ The test method for Base module.

        """

        ob = Base()
        ob1 = Base()
        ob2 = Base(76)
        ob3 = Base()
        ob4 = Base()
        self.assertAlmostEqual(ob.id, 1)
        self.assertAlmostEqual(ob1.id, 2)
        self.assertAlmostEqual(ob2.id, 76)
        self.assertAlmostEqual(ob3.id, 3)
        self.assertAlmostEqual(ob4.id, 4)


if __name__ == "__main__":
    unittest.testmode()
