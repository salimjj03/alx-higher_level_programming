#!/usr/bin/python3
"""


The rextangle module that inherite from base class.


"""


import sys
from models.base import Base


class Rectangle(Base):
    """ The rectangle class.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The class constractor.

        """

        super().__init__(id)
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ The getter method. """
        return self.__width

    @width.setter
    def width(self, value):
        """ The getter method. """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ The getter method. """
        return self.__height

    @height.setter
    def height(self, value):
        """ The getter method. """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ The getter method. """
        return self.__x

    @x.setter
    def x(self, value):
        """ The getter method. """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ The getter method. """
        return self.__y

    @y.setter
    def y(self, value):
        """ The getter method. """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ The area method. """
        return self.__width * self.__height

    def display(self):
        """ The Display method. """
        for a in range(self.__y):
            sys.stdout.write("\n")

        for i in range(self.__height):
            sys.stdout.write(self.__x * " ")
            sys.stdout.write(self.__width * "#")
            sys.stdout.write("\n")

    def __str__(self):
        """ The Display method. """

        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ The Display method. """

        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.__width = args[1] if len(args) >= 2 else self.__width
            self.__height = args[2] if len(args) >= 3 else self.__height
            self.__x = args[3] if len(args) >= 4 else self.__x
            self.__y = args[4] if len(args) >= 5 else self.__y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """ The Display method. """

        return {"x": self.__x, "y": self.__y, "id": self.id,
                "height": self.height, "width": self.width}
