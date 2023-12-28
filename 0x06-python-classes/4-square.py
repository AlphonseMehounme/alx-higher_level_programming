#!/usr/bin/python3
"""Simple Square Module

This is a simple module introducing to class

"""


class Square:
    """Square class

    This is the square class

    """
    def __init__(self, value):
        """init function

        Init function to instanciate

        Args:

        value - size value

        """
        self.sizeset(value)

    @property
    def sizeget(self):
        """size function

        Size function to retrieve the size

        """
        return self.__size

    @size.setter
    def sizeset(self, value):
        """size function

        Size function to get the size

        """
        try:
            self.__size = value
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            if size % 1 != 0:
                raise TypeError("size must be an integer")

    def area(self):
        """Area function

        This function compute
        the area of a square

        Return: Area of the square self

        """
        return self.__size ** 2
