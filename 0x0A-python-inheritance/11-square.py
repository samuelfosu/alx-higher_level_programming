#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inheriting from Rectangle"""
    def __init__(self, size):
        """Instantiation"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """area of the square"""
        return self.__size ** 2

    def __str__(self):
        """description of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
