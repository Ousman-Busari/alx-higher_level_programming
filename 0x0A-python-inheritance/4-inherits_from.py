#!/usr/bin/python3
""" contains the definition of the function inherits_from """


def inherits_from(obj, a_class):
    """ returns true if obj is instance of a class
    that inherited from a_class """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
