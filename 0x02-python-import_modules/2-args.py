#!/usr/bin/python3
import sys

len = len(sys.argv)
if len == 1:
    print("{} arguments.".format(len - 1))
else:
    print("{} arguments:".format(len - 1))
    for i in range(1, len):
        print("{}: {}".format(i, sys.argv[i]))
