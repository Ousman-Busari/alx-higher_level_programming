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
        size.width = value
        size.height = value
