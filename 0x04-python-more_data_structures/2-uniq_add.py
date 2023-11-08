#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for item in set(my_list):
        res = res + item
    return res
