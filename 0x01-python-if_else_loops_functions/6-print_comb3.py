#!/usr/bin/python3
for i in range(1, 10):
    print("{:02d}, ".format(i), end='')
for i in range(1, 8):
    j = i + 1
    while j < 10:
        number = i * 10 + j
        j = j + 1
        print("{}, ".format(number), end='')
print("{}".format(89))
