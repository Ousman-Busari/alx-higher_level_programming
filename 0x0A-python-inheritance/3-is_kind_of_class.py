#!/usr/bin/python3
""" contains the definition of the function is_kind-of_class """

def is_kind_of_class(obj, a_class):
    """ Returns True if obj is a direct or indirect instance of a_class """
    if isinstance(obj, a_class):
        return True
    return False
