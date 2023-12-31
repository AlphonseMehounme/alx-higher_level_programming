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

    def __eq__(self, theother):
        """__eq__ function

        This function return True if the instances are eq
        Flase if not

        """
        if isinstance(theother, Square):
            return self.area() == theother.area()

    def __ne__(self, theother):
        """__ne__ function

        This function True if the instances are not eq
        False if they are

        """
        if isinstance(theother, Square):
            return self.area() != theother.area()

    def __lt__(self, theother):
        """__lt__ function

        Less than function

        """
        if isinstance(theother, Square):
            return self.area() < theother.area()

    def __le__(self, theother):
        """__le__ function

        Less than or equal to function

        """
        if isinstance(theother, Square):
            return self.area() <= theother.area()

    def __gt__(self, theother):
        """__gt__ function

        Greater than function

        """
        if isinstance(theother, Square):
            return self.area() > theother.area()

    def __ge__(self, theother):
        """__ge__ function

        Greater than or equal to function

        """
        if isinstance(theother, Square):
            return self.area() >= theother.area()
