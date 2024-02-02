#!/usr/bin/python3
"""
  Inherits from Module
"""


def inherits_from(obj, a_class):
    """
      inherits_from return True if obj is a subclass
      of a_class, false if not
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
