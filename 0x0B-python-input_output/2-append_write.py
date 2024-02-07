#!/usr/bin/python3
"""
Append file Module
"""


def append_write(filename="", text=""):
    """
      write to file
    """
    with open(filename, 'a') as f:
        write = f.write(text)
    return write
