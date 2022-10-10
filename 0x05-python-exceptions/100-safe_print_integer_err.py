#!/usr/bin/Python3
import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as exc:
        print("Exception:", exc, file=sys.stderr)
        return(False)
    else:
        return(True)