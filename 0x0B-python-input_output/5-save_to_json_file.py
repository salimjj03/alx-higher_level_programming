#!/usr/bin/python3
"""

This Module reads a text file.

"""


import json


def save_to_json_file(my_obj, filename):
    """ This function dose the work.

    """

    with open(filename, "w", encoding="UTF8") as myfile:
        json.dump(my_obj, myfile, ensure_ascii="False")
