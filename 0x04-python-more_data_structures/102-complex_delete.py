#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_d = a_dictionary.copy()
    if a_dictionary:
        for i in new_d:
            if a_dictionary[i] == value:
                del a_dictionary[i]
    return (a_dictionary)
