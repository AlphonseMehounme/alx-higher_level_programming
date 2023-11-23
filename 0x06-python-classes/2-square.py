#!/usr/bin/python3
"""Simple Square Module

This is a simple module introducing to class

"""


class Square:
    """Square class

    This is the square class

    """
    def __init__(self, size=0):
        """Init function

        This is Square init function
        It intanciate the class

        Args:
            size (int): Size of the squre
        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer".format())
