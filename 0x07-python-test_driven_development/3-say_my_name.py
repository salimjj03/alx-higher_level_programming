#!/usr/bin/python3


"""

This module print full name.

"""


def say_my_name(first_name, last_name=""):
    """ The function that print the name.

    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("{} {}".format(first_name, last_name))
