#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)
    sum = 0
    if argc == 1:
        print(0)
    elif argc == 2:
        sum += int(argv[1])
        print(sum)
    else:
        for i in range(1, argc):
            sum  += int(argv[i])
        print(sum)
