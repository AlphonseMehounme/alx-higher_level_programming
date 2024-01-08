#!/usr/bin/python3
"""
    Rectangle Module
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
            Property to get width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Property to set width value
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
           Property to get height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Property to set height value
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
