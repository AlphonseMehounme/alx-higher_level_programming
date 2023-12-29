#!/usr/bin/python3
"""Simple Square Module

This is a simple module introducing to class

"""


class Square:
    """Square class

    This is the square class

    """
    def __init__(self, size=0, position=(0, 0)):
        """init function

        Init function to instanciate

        Args:

        value - size value

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size function

        Size function to retrieve the size

        """
        return self.__size

    @property
    def position(self):
        """position function

        position function to retrieve position

        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """position function

        position function to set position

        """
        try:
            self.__position = value
            if len(value) != 2:
                raise TypeError("position must be a tuple of 2"
                                " positive integers")
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 positive"
                                " integers")

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
            for m in range(self.__position[0]):
                print(" ")
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for j in range(self.__position[0]):
                        print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
