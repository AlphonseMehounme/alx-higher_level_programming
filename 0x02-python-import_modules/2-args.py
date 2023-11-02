#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ags = len(sys.argv) - 1
    if ags == 0:
        print("{} arguments.".format(ags))
    elif ags == 1:
        print("{} argument:".format(ags))
    else:
        print("{} arguments:".format(ags))
    if ags >= 1:
        i = 1
        for j in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[j]))
            i = i + 1
