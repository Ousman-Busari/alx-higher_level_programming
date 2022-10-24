#!/usr/bin/python3
""" A module containing the class Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Definition of class Square """
    def __init__(self, size):
        """ Initializes an instance of the class """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
