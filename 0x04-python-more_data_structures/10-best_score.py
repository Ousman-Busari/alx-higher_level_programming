#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        max = 0
        for key in a_dictionary:
            if a_dictionary[key] > max:
                max_key = key
                max = a_dictionary[key]

        return max_key
