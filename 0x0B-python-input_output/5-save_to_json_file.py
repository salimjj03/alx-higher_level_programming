#!/usr/bin/python3
"""

This Module reads a text file.

"""


import json


def save_to_json_file(my_obj, filename):
    """ This function dose the work.

    """

    myjson = json.dump(my_obj, filename)
