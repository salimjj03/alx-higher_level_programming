#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) > 0:
        my_lists = my_list.copy()
        my_lists.sort(reverse=True)
        return my_lists[0]
