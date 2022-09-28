#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    my_set = set(my_list)
    my_uniq_list = list(my_set)
    for int in my_uniq_list:
        sum += int
    return sum
