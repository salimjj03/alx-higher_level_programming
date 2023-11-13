#!/usr/bin/python3
"""

The test models.

"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class testrectangle(unittest.TestCase):
    """ This test the base modulea.

    """

    def reset(self):
        """ Reset the class attribut. """

        Base.__nb_objects = 0

    def test_rectangle(self):
        """ The test method for Base module.

        """
        
        ob = Rectangle(10, 2)
        ob1 = Rectangle(2, 10, 1)
        ob2 = Rectangle(7, 4, 1, 2)
        ob3 = Rectangle(10, 2, 1, 1, 88)
        self.assertEqual(ob.id, 1)
        self.assertEqual(ob.width, 10)
        self.assertEqual(ob.height, 2)
        self.assertEqual(ob.x, 0)
        self.assertEqual(ob.y, 0)
        self.assertEqual(ob1.id, 2)
        self.assertEqual(ob1.width, 2)
        self.assertEqual(ob1.height, 10)
        self.assertEqual(ob1.x, 1)
        self.assertEqual(ob1.y, 0)
        self.assertEqual(ob2.id, 3)
        self.assertEqual(ob2.width, 7)
        self.assertEqual(ob2.height, 4)
        self.assertEqual(ob2.x, 1)
        self.assertEqual(ob2.y, 2)
        self.assertEqual(ob3.id, 88)
        self.assertEqual(ob3.width, 10)
        self.assertEqual(ob3.height, 2)
        self.assertEqual(ob3.x, 1)
        self.assertEqual(ob3.y, 1)
        self.assertEqual(ob.area(), 20)
        self.assertEqual(ob.display(), '##########\n##########\n')

    def test_value(self):
        """ The test method for Base module. """

        ob = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            ob.width = -1
        with self.assertRaises(ValueError):
            ob.x = -1
        with self.assertRaises(ValueError):
            ob.y = -4
        with self.assertRaises(ValueError):
            ob.height = 0

    def test_type(self):
        """ The test method for Base module. """

        ob = Rectangle(10, 2)
        self.assertRaises(TypeError, ob.width, "7")
        self.assertRaises(TypeError, ob.x, "salim")
        self.assertRaises(TypeError, ob.height, "7")
        self.assertRaises(TypeError, ob.y, "7")
        self.assertRaises(TypeError, ob.width, ["a", 4, 6])
        self.assertRaises(TypeError, ob.width, (2, 4, 5))
        self.assertRaises(TypeError, ob.width, {"salim": 3})
        self.assertRaises(TypeError, ob.width, {3, 2, 4})

