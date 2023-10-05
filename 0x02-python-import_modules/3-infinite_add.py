#!/usr/bin/python3
from sys import argv
n = len(argv)
result = 0;
if __name__ == "__main__":
    for i in range(1, n):
        result = result + int(argv[i])
    print("{}".format(result))
