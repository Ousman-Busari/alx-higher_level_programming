#!/usr/bin/python3
""" A module use to contain a class"""

class Rectangle:
    """ A class definiton of a rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialzes an instance of Rectangle with the given parameters """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves width of a rectagular object"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of a rectangular object"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ Retrieves the heigth of a rectangular object"""
        return self.__width

    @height.setter
    def height(self, value):
        """ Sets the height of a rectangular object"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        """ Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
