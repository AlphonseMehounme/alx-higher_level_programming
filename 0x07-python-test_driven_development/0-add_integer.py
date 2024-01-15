#!/usr/bin/python3
"""
    Add integer module
    This is add integer module
    Add integer function implemented
"""

import math


def add_integer(a, b=98):
    """
        Add integer function
    """
    try:
        a = math.floor(a)
        if a + 1 == a:
            raise OverflowError("Float overflow")
    except TypeError:
        raise TypeError("a must be an integer")
    try:
        b = math.floor(b)
        if b + 1 == b:
            raise OverflowError("Float overflow")
    except TypeError:
        raise TypeError("b must be an integer")
    return a + b
