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

        >>> add_integer(4, 6)
        10
        >>> add_integer(10, 0)
        10
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
