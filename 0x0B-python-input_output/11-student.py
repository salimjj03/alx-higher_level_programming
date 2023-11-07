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

        dic = {}
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

    def reload_from_json(self, json):
        """ Htis is another method.

        """

        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
