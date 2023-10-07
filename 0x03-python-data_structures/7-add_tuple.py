#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_ta = tuple_a + (0, 0)
    new_tb = tuple_b + (0, 0)
    new_tuple = (new_ta[0] + new_tb[0], new_ta[1] + new_tb[1])
    return new_tuple
