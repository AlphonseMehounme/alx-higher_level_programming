#!/usr/bin/python3
for i in range(10):
    j = i + 1
    while j < 10:
        if (10 * i + j) == 89:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end='')
        j = j + 1
