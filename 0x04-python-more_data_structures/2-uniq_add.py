#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    newlist = set(my_list)
    for i in newlist:
        result = result + i
    return result
