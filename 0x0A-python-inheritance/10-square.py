#!/usr/bin/python3
"""
  Square Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
      Class Square
    """
    def __init__(self, size):
        """
          Instanciation function
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
          Calculate area of a Square object
        """
        return self.__size ** 2
