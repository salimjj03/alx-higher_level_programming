#!/usr/bin/python3


"""

The module divide each element of matrix by div.

"""


def matrix_divided(matrix, div):
    """ This functio perform divition

    """

    typeerror = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(typeerror)
    if len(matrix) == 0:
        raise TypeError(typeerror)
    for i in matrix:
        if len(i) != len(matrix[0]) or type(i) != list:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError(typeerror)
    if type(div) != int and type(div) != (float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_max = []
    for a in matrix:
        new_list = list(map(lambda a: round(a / div, 2), a))
        new_max.append(new_list)
    return new_max
