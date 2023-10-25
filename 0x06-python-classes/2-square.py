#!/usr/bin/python3


""" This modul find Sequare 0f number """


class Square:    
    """
    This class find the squareroot of a giving number.

    This class have he follownig method:
    - __init---: initialaze the values of the square root.

    """

    def __init__(self, size=0):
        """
        This method initialize the values of the class.

        :param1: The paramiter that contains the value.

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
