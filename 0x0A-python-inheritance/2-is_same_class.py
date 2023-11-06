#!/usr/bin/python3
"""

This module chech instance of the specified class.

"""


def is_same_class(obj, a_class):
    """ This class does the work.

    """

    if isinstance(type(obj), a_class) == True:
        return True
    else:
        return False
