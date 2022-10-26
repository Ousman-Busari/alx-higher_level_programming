#!/usr/bin/python3
""" Module containing function load_from_json_file """
import json


def load_from_json_file(filename):
    """ creates an object from a JSON file """
    with open(filename) as f:
        return json.load(f)
