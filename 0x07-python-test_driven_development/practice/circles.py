# Compute circle area

from math import pi

def circle(r):
    """
        compute circle area
    """
    if type(r) not in [int, float]:
        raise TypeError("r must be a real number")
    if r < 0:
        raise ValueError("Radius must must >= 0")
    return pi * (r**2)


# Test circle
radius = [1, 5, 0, True, "Yo", 3 + 4j]

for r in radius:
    print("Area of circle of radius {} is {}.".format(r, circle(r)))
