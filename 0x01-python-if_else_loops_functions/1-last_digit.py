#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = number % 10 if number > 0 else number % (-1 * 10)
if l_digit > 5:
    str = "and is greater than 5"
elif l_digit == 0:
    str = "and is 0"
elif l_digit < 6 and l_digit != 0:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {l_digit} {str}")
