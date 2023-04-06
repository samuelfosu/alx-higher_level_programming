#!/usr/bin/python3
"""
A class that defines a Rectangle
"""


class Rectangle:
    """ Defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes the instance
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns the value of the width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Defines the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the value of the height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Defines the height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the Rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """ Calculates the Rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Returns the Rectangle #
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Returns the string represantion of the instance
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when the instance is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
