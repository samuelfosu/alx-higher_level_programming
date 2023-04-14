#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a class Square. """
    def __init__(self, size):
        """ Initializes Square instances.
        Args:
            size(int) - size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Defines and computes the area. """
        return (self.__size ** 2)

    def __str__(self):
        return ("[{}] {}/{}".format(type(self).__name__, self.__size, self.__size))
