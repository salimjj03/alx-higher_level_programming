#!/usr/bin/python3


"""

This module square with #.

"""


def print_square(size):
    """ The function that find the square.

    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
