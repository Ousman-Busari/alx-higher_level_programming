#!/usr/bin/python3

def max_integer(my_list=[]):
    i = len(my_list)
    if i != 0:
        max = my_list[0]
        for j in range(i):
            if my_list[j] > max:
                max = my_list[j]

        return max
