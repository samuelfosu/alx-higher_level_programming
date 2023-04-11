#!/usr/bin/python3
"""Rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation width and height
        as private attributes"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
