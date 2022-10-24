#!/usr/bin/python3
""" Module containing class BaseGeometry"""


class BaseGeometry:
    """ An empty class """
    def area(self):
        """ raises an Exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
