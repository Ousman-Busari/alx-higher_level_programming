#!/usr/bin/python3
""" A module use to contain a class"""


class Rectangle:
    """ A class definiton of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initialzes an instance of Rectangle with the given parameters """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of a rectangular object"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ comapres two rectangles and return the one with a bigger area """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __str__(self):
        """ Defines the string representation of rectangle """

        if self.__width == 0 or self.__height == 0:
            return ('')

        string = []
        for i in range(self.__height):
            for j in range(self.__width):
                string.append(str(self.print_symbol))
            if (i != self.__height - 1):
                string.append('\n')

        return(''.join(string))

    def __repr__(self):
        """ Defines parsable string representation of rectangle objects"""

        return ('Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')')

    def __del__(self):
        """ prints to stdout when a rectangle is deleted """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
