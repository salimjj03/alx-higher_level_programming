#!/usr/bin/python3
"""

This Module reads a text file.

"""


def write_file(filename="", text=""):
    """ This function dose the work.

    """

    with open(filename, "w", encoding="UTF8") as myfile:
        size = myfile.write(text)
    return size
