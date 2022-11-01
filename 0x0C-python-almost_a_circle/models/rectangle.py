#!/usr/bin/python3
"""
Module rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the width of the instance """
        return self.__width
    @width.setter
    def width(self, value):
        """ sets the width of the instance """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the instance """
        return self.__height
    @height.setter
    def height(self, value):
        """ sets the height of the instance """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x attribute of the instance """
        return self.__x
    @x.setter
    def x(self, value):
        """ sets the x attribute of the instance """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the y attribute of the instance """
        return self.__y
    @y.setter
    def y(self, value):
        """ sets the y attribute of the instance """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #
        and taking care of x and y
        """
        string = []
        string.append('\n' * self.__y)
        for i in range(self.__height):
            string.append(' ' * self.__x)
            for j in range(self.__width):
                string.append('#')
            if i != self.__height - 1:
                string.append('\n')
        print(''.join(string))

    def __str__(self):
        """ overrides the defualt string representation """
        string = '[Rectangle] ' + '(' + str(self.id) + ') '
        string += str(self.__x) + '/' + str(self.__y) + ' - '
        string += str(self.__width) + '/' + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args and len(args) > 0:
            if args[0] != None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.width = v
                if k == "height":
                    self.height = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v
