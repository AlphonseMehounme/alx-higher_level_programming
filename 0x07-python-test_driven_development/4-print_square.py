#!/usr/bin/python3
"""
    Print Square Module
"""


def print_square(size):
    """
        print_square function

        Prints a square of size size

        Args:
            size : int that represent the size
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
