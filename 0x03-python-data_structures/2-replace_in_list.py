#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    max_idx = len(my_list) - 1

    if idx >= 0 and idx <= max_idx:
        my_list[idx] = element
        return my_list
