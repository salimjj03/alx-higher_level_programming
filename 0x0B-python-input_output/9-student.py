#!/usr/bin/python3
"""

This Module reads a text file.

"""


class Student():
    """ This function dose the work.

    """

    def __init__(self, first_name, last_name, age):
        """ The custructor method

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Htis is another method.

        """

        return self.__dict__
