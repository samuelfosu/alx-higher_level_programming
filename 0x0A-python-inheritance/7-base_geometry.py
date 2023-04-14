#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """ Defines a class BaseGeometry """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defines a function that validates value. """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
