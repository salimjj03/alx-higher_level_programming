#!/usr/bin/python3
"""

This module chech instance of the specified class.

"""


def inherits_from(obj, a_class):
    """ This class does the work.

    """

    return issubclass(type(obj), a_class) and (type(obj) != a_class)
