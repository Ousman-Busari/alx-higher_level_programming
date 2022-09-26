#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    size = len(my_list)
    if size != 0:
        bol_list = []
        for i in my_list:
            if (i % 2) == 0:
                bol_list.append(True)
            else:
                bol_list.append(False)

        return bol_list
