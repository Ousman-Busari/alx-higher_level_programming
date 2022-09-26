#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
#    if isinstance(my_list, list):
    i = len(my_list)
    while i:
        print("{:d}".format(my_list[i - 1]))
        i -= 1
