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


class Rectangle(BaseGeometry):
    """ This class is sub class of super class.

    """

    def __init__(self, width, height):
        """ This method is a constructor.

        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__height = height
        self.__width = width

    def area(self):
        """ This method return area.

        """

        return self.__height * self.__width

    def __str__(self):
        """ Print classname and area.

        """

        return "[{}] {}/{}" \
            .format(__class__.__name__, self.__width, self.__height)


class Square(Rectangle):
    """ This class is sub class of super class.

    """

    def __init__(self, size):
        """ This method is a constructor.

        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square.

        """

        return self.__size * self.__size

    def __str__(self):
        """ Print classname and area.

        """

        return "[{}] {}/{}" \
            .format(__class__.__name__, self.__size, self.__size)
