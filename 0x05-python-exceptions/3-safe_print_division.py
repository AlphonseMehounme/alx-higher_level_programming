#!/usr/bin/python3
def safe_print_division(a, b):
    i = 0
    try:
        return a / b
    except ZeroDivisionError:
        i = i + 1
        return None
    finally:
        if (i):
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(a / b))
