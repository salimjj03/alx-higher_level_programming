#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx <= len(my_list) and idx >= 0:
        for i in range(len(my_list)):
            if i == idx:
                my_list[i] = element
                return my_list
    return my_lsit
