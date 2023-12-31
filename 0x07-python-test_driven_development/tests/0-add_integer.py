"""
    Add integer module
    This is add integer module
    Add integer function implemented

"""
import math
#from '0-add_integer' import add_integer

def add_integer(a, b=98):
    """
>>> add_integer(5, 15)
20
>>> add_integer(6, 2)
8
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
