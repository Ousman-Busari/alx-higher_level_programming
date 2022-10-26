#!/usr/bin/python3
""" Module containing function save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ writes an object to a text file,
    using JSON representaion
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
