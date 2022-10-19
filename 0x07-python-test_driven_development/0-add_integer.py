#!/usr/bin/python3
"""
This module contains a function that adds two integers
or float(of the rigth value)

The name of the function is add_integer
"""

def add_integer(a, b):
    """
    add two integers - or float of the right value - a and b
    if any or both are of the wrong type or value, an error is raised.
    Otherwise, returns the sum of the two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
