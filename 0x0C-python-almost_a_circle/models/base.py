#!/usr/bin/python3
"""


This module containe the base class.


"""


import json


class Base:
    """ This is the base class.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the constructor method

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ This is the constructor method

        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ This is the constructor method

        """

        ls = []
        if list_objs:
            for i in list_objs:
                ls.append(i.to_dictionary())
        else:
            pass
        with open(cls.__name__+".json", "w") as f:
            f.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """ This is the constructor method

        """

        ls = []
        if json_string:
            return [json.loads(json_string)]
        else:
            return ls

    @classmethod
    def create(cls, **dictionary):
        """ This is the constructor method

        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This is the constructor method

        """
        
        ls = []
        with open(cls.__name__+".json", "r") as f:
            ls.append(cls.create({cls.from_json_string(f.readline())}))

        return ls
