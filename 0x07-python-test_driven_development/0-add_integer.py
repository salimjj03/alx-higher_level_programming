#!/usr/bin/python3


"""

This mode find the sum of Tow numbers

"""


def add_integer(a, b=98):
    """ The function find the sum of two integers.

    """
    if type(a) is not int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a + b)
