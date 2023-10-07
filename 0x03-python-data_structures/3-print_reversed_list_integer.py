#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = my_list.copy()
    reverse_list.reverse()
    for i in reverse_list:
        print("{:d}".format(i))
