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

    def area(self):
        """ calculates and returns the area of a rectangular object """
        return self.__width * self.__height

    def __str__(self):
        string = '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
        return string
