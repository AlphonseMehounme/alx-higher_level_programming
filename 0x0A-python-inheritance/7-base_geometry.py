#!/usr/bin/python3
"""
  Base Geometry Module
"""


class BaseGeometry:
    """
      BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            error_msg = "{} must be an integer".format(name)
            raise TypeError(error_msg)
        if value <= 0:
            error_msg = "{} must be greater than 0".format(name)
            raise ValueError(error_msg)
