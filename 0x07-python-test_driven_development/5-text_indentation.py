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
    i = 0

    while i < len(text):
        print(text[i], end='')

        if text[i] in char_list:
            print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
