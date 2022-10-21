#!/usr/bin/python3
""" Module contaning a locked class """

class LockedClass:
    """ A class with no dictionary, only a memory reservation
    for an attribte called first_name
    All instances of this class also inherit this property
    """
    __slot__ = ['first_name']
