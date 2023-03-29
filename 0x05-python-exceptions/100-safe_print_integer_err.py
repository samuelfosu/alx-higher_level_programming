#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys


def safe_print_integer_err(value):
    """ Prints an integer.
    Args:
    value - value to be printed
    Returns:
    True - if value has been printed correctly as int
    False - otherwise in stderr preceeded by Exception
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
