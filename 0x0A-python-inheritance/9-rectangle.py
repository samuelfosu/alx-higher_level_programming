#!/usr/bin/python3
"""Module for Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle from BaseGeometry Class"""
    def __init__(self, width, height):
        """Instantiation with width and height
        as private attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
