#!/usr/bin/python3


""" This modul find Sequare 0f number """


class Square:    
    """ This class find the squareroot of a giving number.

    This class have he follownig method attribute

    Attributes:
        attr1 (str): Description of `attr1`.

    """

    def __init__(self, size=0):
        """ Discription of the __init__ method.

        The __init__ method initialize the values of the class.

        Args:
            param1 (size): Description of `size.

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
