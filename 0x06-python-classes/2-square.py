#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """class representation of a Square

    Attributes:
               __size(int): size of the side of the square
    """
    def __init__(self, size=0):
        """Initiliaze an instance of the square

        Args:
             size(int): size of the side of the square

        Returns:
                None
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
