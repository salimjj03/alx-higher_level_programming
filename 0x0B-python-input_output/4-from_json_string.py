#!/usr/bin/python3
"""

This Module reads a text file.

"""


import json


def from_json_string(my_str):
    """ This function dose the work.

    """

    myjson = json.loads(my_str)
    return myjson
