#!/usr/bin/python3
"""
    Just a practice module
"""


numbers = [1, 2, 3, 4, 5]

def puresquarelist(alist):
    newlist = []
    for i in range(len(alist)):
        newlist += [alist[i] * alist[i]]
    return newlist

liste = puresquarelist(numbers)
print(liste)
# numbers is still the same
print(numbers)
