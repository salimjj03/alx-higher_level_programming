#!/usr/bin/python3


"""

This module print newline when one of (: ? .)
is found

"""


def text_indentation(text):
    """ The function that dose the work.

    """

    if type(text) != str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i - 1] not in ".?:" and text[i] != " ":
            print(text[i], end="")
            if text[i] in ".?:":
                print("\n")
