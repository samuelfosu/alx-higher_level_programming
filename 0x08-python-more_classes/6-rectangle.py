#!/usr/bin/python3
"""
A class that defines a Rectangle
"""


class Rectangle:
    """ Class defines a rectangle """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes instance
        Args:
            width: rectangle width
            height: rectangle height
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns value of the width
        Returns:
            rectangle width
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ Defines width
        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns height value
        Returns:
            rectangle height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Defines height
        Args:
            value: height
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates area
        Returns:
            rectangle area
        """

        return self.width * self.height

    def perimeter(self):
        """ Calculates perimeter
        Returns:
            rectangle perimeter
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ Returns rectangle value
        Returns:
            string of rectangle
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Returns string represantion of instance
        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Prints message when instance is deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
