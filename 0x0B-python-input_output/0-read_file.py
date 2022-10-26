#!/usr/bin/python3
""" Contains the function read_file """


def read_file(myfile):
    """ reads from a file and prints its text out
    to the stdout

    """
    with open(myfile) as f:
        print(f.read(), end='')
