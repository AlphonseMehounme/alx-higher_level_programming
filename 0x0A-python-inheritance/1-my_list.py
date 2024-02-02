#!/usr/bin/python3
"""
  MyList Module
"""


class MyList(list):
    """
      MyList class that inherit from list
    """
    def print_sorted(self):
        """
          print_sorted function prints
          the sorted version of an object
        """
        print(sorted(self))
