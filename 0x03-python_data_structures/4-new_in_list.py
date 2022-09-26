#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    if idx < 0:
        return

    max_idx = len(my_list) - 1

    if idx > max_idx:
        return

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
