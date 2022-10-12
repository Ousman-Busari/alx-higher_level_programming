#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """class representation of a Square

    Attributes:
               size(int): size of the side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initiliazes an instance of the square

        Args:
             size(int): size of the side of the square
             position(tuple): position of the square object

        Returns:
                None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves the property of attribute position of a square object

        Return:
               position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the property of attribute position of a square object

        Args:
             value(tuple): the new location of the square object

        Return:
              None
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(point) is int for point in value) or
                not all(point >= 0 for point in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Calculates the area of the square

        Return:
               area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #

        Return:
               None
        """

        if self.size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.size):
            print(" " * self.__position[0], end='')
            for j in range(self.size):
                print('#', end='')
            print()
