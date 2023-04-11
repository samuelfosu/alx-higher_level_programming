#!/usr/bin/python3
""" class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inheriting from Rectangle"""
    def __init__(self, size):
        """Instantiation instances"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
