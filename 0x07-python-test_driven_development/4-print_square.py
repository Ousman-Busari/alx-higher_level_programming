#!/usr/bin/python3
"""
This module contains a function that prints a square with
character #

The name of function is print_square
"""


def print_square(size):
    """
    Prints out a square of size 'size' using character '#'

    if size if of wrong value or type, appropriate error is raised
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
