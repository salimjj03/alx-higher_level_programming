#!/usr/bin/python3
for n in range(9):
    for i in range(n+1, 10):
        print("{}{}".format(n, i), end=', ' if n != 8 else '\n')
