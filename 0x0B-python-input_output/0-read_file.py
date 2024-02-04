#!/usr/bin/python3
"""
  Read Text File Module
"""


def read_file(filename=""):
    """
      reads filename and prints the content
    """
    with open(filename, 'r') as file:
        content = file.read()
        print(content, end="")
