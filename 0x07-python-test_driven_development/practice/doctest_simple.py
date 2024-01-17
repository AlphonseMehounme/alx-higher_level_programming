# doctest_simple

__test__ = {

'numner': """
>>> function(2, 3)
6

>>> function(5, 2)
10
""",

'function': 'function'
}

def function(a, b):
    """
    >>> function('a', 2)
    'aa'
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

