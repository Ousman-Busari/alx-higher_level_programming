#!/usr/bin/python3
""" Module containing a modified version of class int, MyInt """


def MyInt(int):
    """ A modified instance of int"""

    def __eq__(self, other):
        """ overrides and inverts the conditional check == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ overrides and inverts the conditional check != """
        return super().__eq__(other)
