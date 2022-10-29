#!/usr/bin/python3
""" Module containing the function class_to_json """


def class_to_json(obj):
    """ returns the dictionary representation of obj """
    return obj.__dict__
