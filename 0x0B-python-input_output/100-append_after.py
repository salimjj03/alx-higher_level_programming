#!/usr/bin/python3
"""

This Module reads a text file.

"""


def to_json_string(my_obj):
    """ This function dose the work.

    """

     text = ""
    with open(filename, "r", encoding='UTF8') as myfile:
        line = myfile.read()
    for i in line:
        if i.find(search_string) != -1:
            text += i + new_string
        else:
            text += i
    with open(filename, "w", encoding='UTF8') as myfile:
        myfile.write(text)
