#!/usr/bin/python3
def lookup(obj):
    """ Returns the list of available attributes
        and methods of an object
    Args:
        obj: class instance
    Returns:
        Attributes
    """

    return dir(obj)
