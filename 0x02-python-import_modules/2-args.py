#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    len = len(argv)
    if len == 1:
        print("{} arguments.".format(len - 1))
    else:
        print("{} arguments:".format(len - 1))
        for i in range(1, len):
            print("{}: {}".format(i, argv[i]))
