#!/usr/bin/python3
"""
This module contains a function that prints a new line after
any of these characters ., ? and : is encountered

The name of function is text_indentation
"""

def text_indentation(text):
    """
    Prints out a text provided as argument
    and starts printimg on a new line if any
    of the characters is encountered

    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    char_list = ['.', '?', ':']
    prev_i = None

    for i in text:
        if prev_i in char_list and i == ' ':
            print()
            continue
        if i in char_list:
            print(i)
            prev_i = i
        else:
            print(i, end='')
            prev_i = i
