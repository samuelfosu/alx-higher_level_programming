#!/usr/bin/python3
"""

A function that adds 2 numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integers

    Args:
        a: num one
        b: num two

    Returns:
        num one plus num two

    Raises:
        TypeError: If a or b aren't integers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
