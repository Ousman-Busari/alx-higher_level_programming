#!/usr/bin/python3

def weight_average(my_list=[]):
    cum_total = 0
    weight_total = 0
    if len(my_list) == 0:
        return 0
    for tup in my_list:
        cum_total += (tup[0] * tup[1])
        weight_total += tup[1]

    return (cum_total / weight_total)
