#!/usr/bin/python3
"""
This module contains a function that prints out
a user full name (first name and last name)

The name of function is say_my_name
"""

def say_my_name(first_name, last_name=''):
    """
    Prints out first name and last name (if provided)
    based on the condition that they are both strings

    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print("{} {}".format(first_name, last_name))
