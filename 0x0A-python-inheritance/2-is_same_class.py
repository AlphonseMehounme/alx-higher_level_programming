#!/usr/bin/python3
"""
  Is Same Class Object
"""


def is_same_class(obj, a_class):
    """
      function that state if obj is of
      a_class or not

      Args:
        obj : object
        a_class : class

      Return: True if true
      False if not
    """
    if type(obj) == a_class:
        return True
    else:
        return False
