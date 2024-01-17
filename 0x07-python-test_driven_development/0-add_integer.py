#!/usr/bin/python3
"""
    Add integer module
    This is add integer module
    Add integer function implemented
"""


def add_integer(a, b=98):
    """
        Add integer function
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
