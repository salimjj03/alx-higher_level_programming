#!/usr/bin/python3


""" This modul find Sequare 0f number """


class Square:    
    """Find the squareroot of a number"""

    def __init__(self, size=0):
        """This method initialize values"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This Method find area"""
        return self.__size ** 2
