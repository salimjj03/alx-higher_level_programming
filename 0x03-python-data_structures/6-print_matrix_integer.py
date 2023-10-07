#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        len_i = len(i) - 1
        for j in range(len(i)):
            if j != len_i:
                print("{:d}".format(i[j]), end=" ")
            else:
                print("{:d}".format(i[j]), end="")
        print()
