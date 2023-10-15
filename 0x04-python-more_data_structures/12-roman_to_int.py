#!/usr/bin/python3
def roman_to_int(roman_string):
    n = 0
    if roman_string == '' or !roman_string:
        return 0
    digit = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in digit:
            if i + 1 < len(roman_string) and roman_string[i + 1] in digit and \
                    digit[roman_string[i]] < digit[roman_string[i + 1]]:
                n = n - digit[roman_string[i]]
            else:
                n = n + digit[roman_string[i]]
        else:
            return 0
    return n
