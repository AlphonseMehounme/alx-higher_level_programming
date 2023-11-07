#!/usr/bin/python
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list = new_list + [True]
        else:
            new_list = new_list + [False]
    return new_list
