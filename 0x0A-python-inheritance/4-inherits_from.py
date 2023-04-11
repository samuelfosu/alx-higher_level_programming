#!/usr/bin/python3
"""Function that returns True/False if obj is an instance of a_class"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a_class
        False, otherwise"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
