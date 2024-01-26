#!/usr/bin/python3
""" this module  finds a peak in a list of nunsorted integer. """


def find_peak(list_of_integers):
    """ this module  finds a peak in a list ."""

    if list_of_integers:
        ln = len(list_of_integers)
        i = 0

        for n in list_of_integers:
            if i == 0 and ln > 1 and n >= list_of_integers[i + 1]:
                return n
            elif i == 0 and ln == 2 and n < list_of_integers[i + 1]:
                return list_of_integers[i + 1]
            elif ln - i <= 1 and n >= list_of_integers[i - 1]:
                return n
            elif n >= list_of_integers[i - 1] and n >= list_of_integers[i + 1]:
                return n
            i = i + 1
