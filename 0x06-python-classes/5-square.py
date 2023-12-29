#!/usr/bin/python3
"""Simple Square Module

This is a simple module introducing to class

"""


class Square:
    """Square class

    This is the square class

    """
    def __init__(self, size=0):
        """init function

        Init function to instanciate

        Args:

        value - size value

        """
        self.size = size

    @property
    def size(self):
        """size function

        Size function to retrieve the size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size function

        Size function to get the size

        """
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        else:
            if value % 1 != 0:
                raise TypeError("size must be an integer")

    def area(self):
        """Area function

        This function compute
        the area of a square

        Return: Area of the square self

        """
        return self.__size ** 2

    def my_print(self):
        """My print function

        This function print the square to stdout with #

        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
