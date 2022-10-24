#!/usr/bin/python3
""" module containing the definition of the class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ definition of class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes an instance of the class """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
