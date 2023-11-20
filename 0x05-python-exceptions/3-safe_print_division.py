#!/usr/bin/python3
def safe_print_division(a, b):
    i = 0
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        i = i + 1
        return None
    finally:
        if (i):
            print("Inside result: None")
        else:
            print("Inside result: ", a / b)
