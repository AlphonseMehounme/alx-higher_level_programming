#!/usr/bin/python3
"""
    Rectangle Module

    To represente a rectangle
"""


class Rectangle:
    """
        Rectangle Class
    """
    def __init__(self, width=0, height=0):
        """
            Instanciation function
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Function to get width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Function to set width value
        """
        try:
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        except TypeError:
            raise TypeError("width must be an integer")
        else:
            if value % 1 != 0:
                raise TypeError("width must be an integer")

    @property
    def height(self):
        """
            Function to get height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Function to set height value
        """
        try:
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        except TypeError:
            raise TypeError("height must be an integer")
        else:
            if value % 1 != 0:
                raise TypeError("height must be an integer")

    def area(self):
        """
            Compute area
        """
        return self.__width * self.__width

    def perimeter(self):
        """
            Compute the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
            Function that allow printing Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str = str + "#"
            if i != self.__height - 1:
                str = str + "\n"
        return str

    def __repr__(self):
        """
            repr function
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
