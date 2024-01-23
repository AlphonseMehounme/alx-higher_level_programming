#!/usr/bin/python3
"""
    Just a practice module
"""


numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] *= numbers[i]
print(numbers)

# We can also access index and values in the same time
# with enum

for i, value in enumerate(numbers):
    numbers[i] *= value
print(numbers)
