#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    newlist = []
    while i < list_length:
        try:
            newlist = newlist + [my_list_1[i] / my_list_2[i]]
        except TypeError:
            print("wrong type".format())
            newlist = newlist + [0]
        except ZeroDivisionError:
            print("division by 0".format())
            newlist = newlist + [0]
        except IndexError:
            print("out of range")
            newlist = newlist + [0]
        finally:
            i = i + 1
    return newlist
