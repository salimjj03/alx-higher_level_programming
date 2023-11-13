#!/usr/bin/python3
"""


This module containe the base class.


"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is the base class.

    """

    def __init__(self, size, x=0, y=0, id=None):
        """ This is the constructor method

        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ The Display method. """

        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ The Display method. """

        return self.width

    @size.setter
    def size(self, value):
        """ The Display method. """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ The Display method. """

        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.heigth = args[1] if len(args) >= 2 else self.height
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ The Display method. """

        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
