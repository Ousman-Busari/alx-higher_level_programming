#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    i = my_list.index(search)
    new_list[i] = replace
    return new_list
