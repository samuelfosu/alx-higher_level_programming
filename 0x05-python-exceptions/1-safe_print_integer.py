#!/usr/bin/python3
# 1-safe_print_integer.py

def safe_print_integer(value):
    """ Prints an integer with "{:d}".format().

    Args:
    value - value to be printed

    Returns:
    True if value has been correctly printed as integer
    """
    try:
        print("{:d}".format(value))
        return {True}
    except (ValueError, TypeError):
        return (False)
