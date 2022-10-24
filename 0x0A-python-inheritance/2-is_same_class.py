#!/usr/bin/python3
""" contains the definition of the function is_same_class """


def is_same_class(obj, a_class):
    """ returns True is obj is exactly an instance of a_class """
    if type(obj) == a_class:
        return True
    return False
