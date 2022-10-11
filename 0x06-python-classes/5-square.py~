#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """class representation of a Square

    Attributes:
               size(int): size of the side of the square
    """
    def __init__(self, size=0):
        """Initiliazes an instance of the square

        Args:
             size(int): size of the side of the square

        Returns:
                None
        """
        self.size = size

    def area(self):
        """Calculates the area of the square

        Return:
               area of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """retrieves the property of attribute size of a square object

        Return:
               size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the property of attribute size of a square object

        Args:
             value(int): the new size of the square object

        Return:
              None
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
