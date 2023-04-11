#!/usr/bin/python3
"""Function that returns True/False if obj is an instance of a_class"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance of a_class
        False, otherwise"""
    return isinstance(obj, a_class)
