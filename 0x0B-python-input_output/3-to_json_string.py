#!/usr/bin/python3
"""

This Module reads a text file.

"""


import json


def to_json_string(my_obj):
    """ This function dose the work.

    """

    myjson = json.dumps(my_obj)
    return myjson
