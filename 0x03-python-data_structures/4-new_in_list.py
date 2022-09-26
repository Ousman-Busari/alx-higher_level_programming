#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    max_idx = len(my_list)
    if idx >= 0 and idx < max_idx:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
