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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = math.floor(a)
    try:
        b = math.floor(b)
    except TypeError:
        raise TypeError("b must be an integer")
    return a + b
