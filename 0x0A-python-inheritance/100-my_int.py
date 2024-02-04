#!/usr/bin/python3
"""
  MyInt Module
"""


class MyInt(int):
    """
      MyInt class that inherits from int
    """
    def __init__(self, value):
        """
          Instanciation method
        """
        self.value = value

    def __eq__(self, other):
        """
          Define == behavior between two MyInt objects
        """
        if isinstance(other, MyInt):
            return not self.value == other.value
        return True

    def __ne__(self, other):
        """
          Define != behavior between two MyInt objects
        """
        return not self.__eq__(other)
