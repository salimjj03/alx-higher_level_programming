#!/usr/bin/python3


"""This modul find Sequare 0f number."""


class Square:
    """Find the squareroot of a number."""

    def __init__(self, size=0, position=(0, 0)):
        """This method initialize values"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        self.__position = position

    def area(self):
        """This Method find area"""
        return self.__size ** 2

    @property
    def size(self):
        """The summary line for a class docstring should fit on one line."""
        return self.__size

    @size.setter
    def size(self, value):
        """The summary line for a class docstring should fit on one line."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """The summary line for a class docstring should fit on one line."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end="")
            for i in range(self.__size):
                print("{}".format(self.__position[0] * " "), end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
    @property
    def position(self):
        """The summary line for a class docstring should fit on one line."""
        return self.__position

    @position.setter
    def position(self, value):
        """The summary line for a class docstring should fit on one line."""
        if (type(value) is not tuple or len(value) != 2 or
               type(value[0]) is not int or
               type(value[1]) is not int or
               value[0] < 0 or value[1] < 0):
               raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
