#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            new_list = new_list + [element]
        else:
            new_list = new_list + [my_list[i]]
    return new_list
