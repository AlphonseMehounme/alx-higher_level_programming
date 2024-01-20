#!/usr/bin/python3
"""
    Text indentation module
"""


def text_indentation(text):
    """
        text_indentation function
        Print text with two new line if the character is ., ? or :

        Args:
            text : String to print
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
            i += 1
        i += 1
