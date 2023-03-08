#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# lastdigit = repr(number)
# lastdigit = lastdigit[-1]
# lastdigit = int(lastdigit)
lastdigit = number % 10
if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
if lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
elif lastdigit < 6:
    print(
            f"Last digit of {number} is {lastdigit} and is "
            f"less than 6 and not 0"
        )
