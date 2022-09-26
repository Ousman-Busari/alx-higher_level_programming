#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if idx < 0:
        return

    max_idx = len(my_list) - 1

    if idx > max_idx:
        return

    my_list[idx] = element

    return my_list
