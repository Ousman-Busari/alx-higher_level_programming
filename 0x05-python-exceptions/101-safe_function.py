#!/usr/bin/Python3
import sys


def safe_function(fct, *args):

    try:
        return (fct(*args))
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as exc:
        print("Exception:", exc, file=sys.stderr)
        return(False)
