#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    ln = len(my_list) - 1
    for i in range(ln, -1, -1):
        print("{:d}".format(my_list[i]))
