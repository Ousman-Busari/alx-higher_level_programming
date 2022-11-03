#!/usr/bin/python3
"""
square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a new instance of Sqaure """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ str representation of an instance of Sqaure """
        string = "[Square] ({}) {}/{} - {}".format(self.id,
                                                   self.x, self.y, self.size)
        return string

    def update(self, *args, **kwargs):
        """ updates the instances of the attribute """
        if args and len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for k, v in kwargs.items():
                if k == "id" and v is not None:
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of Square instances """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
            }
