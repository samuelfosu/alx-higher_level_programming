#!/usr/bin/python3
""" defines a rectangle """

class Rectangle:
    """ Class defines rectangle """

    def __init__(self, width=0, height=0)
    """ initializes instance """

    self.width = width
    self.height = height

    @property
    def width(self):
    """ returns width value """

    return self.__width

    @width.setter
    def width(self, value):
    """ defines width """

    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

    @property
    def height(self):
        """ returns height value """

        return self.__height

    @height.setter
    def height(self, value):
        """ defines height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method calculates area """

        return self.width * self.height

    def perimeter(self):
        """ calaculate perimeter """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ returns the Rectangle """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method returns string represantion """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
