#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ Function returns True/False if obj is an instance of a_class
    
    Args:
        obj: object
        a_class: class
    
    Returns:
        True if obj is instance of a_class
        False, otherwise
    """
    return isinstance(obj, a_class)
