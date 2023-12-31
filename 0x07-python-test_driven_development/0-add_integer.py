#!/usr/bin/python3
"""
    Add integer module
    This is add integer module
    Add integer function implemented

>>> add_integer(3, 7)
10
"""
import math
def add_integer(a, b=98):
    """
        Add integer function
    """
    try:
        a = math.floor(a)
    except:
        raise TypeError("a must be an integer")
    try:
        b = math.floor(b)
    except:
        raise TypeError("b must be an integer")
    return a + b
