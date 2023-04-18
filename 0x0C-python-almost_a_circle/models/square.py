#!/usr/bin/python3
"""
Implements Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the class square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the size. """
        return (self.width)

    @size.setter
    def size(self, value):
        """ Sets the value. """
        self.validate_attr("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns a fine print. """
        return ("[{}] ({}) {}/{} - {}"
                .format(type(self).__name__, self.id, self.x, self.y,
                        self.width))

    def update(self, *args, **kwargs):
        """ Assigns value to attributes. """
        if (len(args) == 0):
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
    def to_dictionary(self):
        """ to_dictionary method """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
