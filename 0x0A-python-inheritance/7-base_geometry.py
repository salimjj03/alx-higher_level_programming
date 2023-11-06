#!/usr/bin/python3
"""

This module chech instance of the specified class.

"""


class BaseGeometry:
    """ This class does the work.

    """

    def area(self):
        """ Raise exception.

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This validate int.

        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
