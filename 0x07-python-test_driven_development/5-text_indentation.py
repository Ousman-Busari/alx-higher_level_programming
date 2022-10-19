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

    for i in range(len(text)):
        if prev_i in char_list and text[i] == ' ':
            print()
            continue
        if text[i] in char_list and text[i + 1] == ' ':
            print(text[i])
            prev_i = text[i]
        else:
            print(text[i], end='')
            prev_i = text[i]
