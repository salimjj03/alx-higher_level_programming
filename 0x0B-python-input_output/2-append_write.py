#!/usr/bin/python3
"""

This Module reads a text file.

"""


def append_write(filename="", text=""):
    """ This function dose the work.

    """

    with open(filename, "a", encoding="UTF8") as myfile:
        size = myfile.write(text)
    return size
