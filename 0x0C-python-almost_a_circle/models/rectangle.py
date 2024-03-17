#!/usr/bin/python3
"""
  Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """
      Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
          Constructor of rectangle objects
        """
        super().__init__(id)
        allarg = ['width', 'height', 'x', 'y']
        allargval = [width, height, x, y]
        for n in range(len(allarg)):
            if type(allargval[n]) != int:
                raise TypeError(f"{allarg[n]} must be an integer")
        allarg1 = ['width', 'height']
        allargval1 = [width, height]
        for m in range(len(allarg1)):
            if allargval1[m] <= 0:
                raise ValueError(f"{allarg1[m]} must be > 0")
        allarg2 = ['x', 'y']
        allargval2 = [x, y]
        for j in range(len(allarg2)):
            if allargval2[j] < 0:
                raise ValueError(f"{allarg2[j]} must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
          width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
          width setter
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
          height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
          height setter
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
          x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
          x setter
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
          y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
          y setter
        """
        if type(x) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
          Compute the area of rectangle
        """
        return self.__width * self.__height
