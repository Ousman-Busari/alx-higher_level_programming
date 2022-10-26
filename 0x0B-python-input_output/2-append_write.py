#!/usr/bin/python3
""" Contains the function append_write """


def append_write(filename="", text=""):
    """ write text to filename, or create a new one if it doesn't exist,
    and return the number of characters written in to the file

    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
