#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None
    return (sorted(a_dictionary.items(), key=lambda item: item[1]))[-1][0]
