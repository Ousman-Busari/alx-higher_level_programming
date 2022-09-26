#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return
    max_idx = len(my_list) - 1
    if idx > max_idx:
        return
    return my_list[idx]
