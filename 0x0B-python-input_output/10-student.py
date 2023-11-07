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

    def to_json(self, attrs=None):
        """ Htis is another method.

        """

        ls = {}
        if type(attrs) != list:
            return self.__dict__

        else:
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            for j in self.__dict__:
                if j in attrs:
                    dic[j] = self.__dict__[j]
        return dic
