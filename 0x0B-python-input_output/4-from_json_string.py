#!/usr/bin/python3
""" Module containing function from_json_string """
import json


def from_json_string(my_str):
    """ returns the python object representation
    of json string my_str
    """
    return json.loads(my_str)
