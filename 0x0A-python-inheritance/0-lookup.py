#!/usr/bin/python3
"""
    Module Lookup
"""


def lookup(obj):
    """
      lookup function : 
      find the availavle attr and methods of obj

      Args: 
        obj : Object to look attr and methods available for

      Return:
        Return a list of available attr and methods for obj
    """
    return dir(obj)
