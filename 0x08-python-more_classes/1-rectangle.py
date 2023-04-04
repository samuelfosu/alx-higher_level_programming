#!/usr/bin/python3
"""
Class Retangle

"""

class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize the instance"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Return the width"""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Return the height"""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
