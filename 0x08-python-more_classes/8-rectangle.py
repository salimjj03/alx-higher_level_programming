#!/usr/bin/python3


"""

This is empty class

"""


class Rectangle:
    """ defines an empty class rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initialize the values. """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ This method get the width. """

        return self.__width

    @width.setter
    def width(self, value):
        """ This method set the width. """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This method get the heiget. """

        return self.__height

    @height.setter
    def height(self, value):
        """ This method set the height. """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This method return area of rectangle. """

        return self.__width * self.__height

    def perimeter(self):
        """ This method return perimeter of rectangle. """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ This print te values of tha object. """

        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += (str(self.print_symbol))
            if i < (self.__height - 1):
                string += "\n"
        return string

    def __repr__(self):
        """ This print te values of tha object. """

        return "Rectangle(" + str(self.__width) + ", "\
                            + str(self.__height) + ")"

    def __del__(self):
        """ This print te values of tha object. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ This print te values of tha object. """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
