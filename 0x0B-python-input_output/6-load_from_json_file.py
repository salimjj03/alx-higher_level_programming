#!/usr/bin/python3
"""

This Module reads a text file.

"""


import json


def load_from_json_file(filename):
    """ This function dose the work.

    """

    with open(filename, "r", encoding="UTF8") as myfile:
        return json.load(myfile)
