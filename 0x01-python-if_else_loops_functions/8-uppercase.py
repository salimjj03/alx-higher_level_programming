#!/usr/bin/python3
def uppercase(str):
    for n in range(len(str)):
        print("{}".format(chr(ord(str[n]) - 32))
              if ord(str[n]) > 96 and ord(str[n]) < 123
              else "{}".format(str[n]), end='')
    print("{}".format(''))
