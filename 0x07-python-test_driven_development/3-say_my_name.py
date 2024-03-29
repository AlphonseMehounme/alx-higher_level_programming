#!/usr/bin/python3
"""
    Say My Name Module
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name function

        Prints My name is <first name> <last name>

        Args:
            first_name: string
            last_name: string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
