#!/usr/bin/python3
"""
Rectangle is a subclass of Base class
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle defines a class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width property"""
        self.validate_attr("width", value)
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height property"""
        self.validate_attr("height", value)
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the x property"""
        self.validate_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """Gets the y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the y property"""
        self.validate_attr("y", value)
        self.__y = value

    def area(self):
        """Defines the area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints Rectangle instance with # char to stdout"""
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute"""
        if (len(args) == 0):
            for key, value in kwargs.items():
                setattr(self, key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """Prints a fine print"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @staticmethod
    def validate_attr(attr, value):
        """Validates attributes and values"""
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(attr))
        elif (attr == "width" or attr == "height"):
            if (value <= 0):
                raise ValueError("{} must be > 0".format(attr))
        elif (attr == "x" or attr == "y"):
            if (value < 0):
                raise ValueError("{} must be >= 0".format(attr))

    def to_dictionary(self):
        """Returns the dict. representation of a Rectangle"""
        return {
                "id": self.id,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
