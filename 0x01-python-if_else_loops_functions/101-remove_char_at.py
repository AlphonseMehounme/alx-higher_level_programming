#!/usr/bin/python3
def remove_char_at(str, n):
    strnew = ""
    for i in range(len(str)):
        if i != n:
            strnew = strnew + str[i]
    return strnew
