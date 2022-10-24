#!/usr/bin/python3
""" Module containing class MyList """


class MyList(list):
    """ Defines the class MyList that inherits
    from the built-in classs List
    """
    def print_sorted(self):
        """ prints a list in asorted order """
        print(sorted(self))
