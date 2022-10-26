#!/usr/bin/python3
""" Module containing function to_json_string """
import json


def to_json_string(my_obj):
    """ returns the json representation of my_obj """

    return json.dumps(my_obj)
