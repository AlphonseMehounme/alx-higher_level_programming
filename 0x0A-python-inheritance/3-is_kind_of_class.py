#!/usr/bin/python3
"""
  Is Kind Of Class Object
"""


def is_kind_of_class(obj, a_class):
    """
       Return True if obj is instance of a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
