#!/usr/bin/python3
"""

This Module reads a text file.

"""


def read_file(filename=""):
    """ This function dose the work.

    """

    with open(filename, "r", encoding="UTF8") as myfile:
        print(myfile.read(), end="")
