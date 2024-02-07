#!/usr/bin/python3
"""
  Write file Module
"""


def write_file(filename="", text=""):
    """
      write to file
    """
    with open(filename, 'w') as f:
        write = f.write(text)
    return write
