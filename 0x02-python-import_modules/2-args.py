#!/usr/bin/python3
import sys
argv = sys.argv

if __name__ == "__main__":
    argc = len(argv)
    if argc == 1:
        print("{} arguments.".format(argc - 1))
    else:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
