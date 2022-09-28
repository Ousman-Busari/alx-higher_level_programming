#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None and isinstance(a_dictionary, dict):
        return (sorted(a_dictionary.items())[-1][0])
