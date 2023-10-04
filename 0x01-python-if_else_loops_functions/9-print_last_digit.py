#!/usr/bin/python3
def print_last_digit(number):
    l_digit = number % 10 if number >= 0 else (number % (10 * -1)) * -1
    print("{}".format(l_digit), end='')
    return l_digit
