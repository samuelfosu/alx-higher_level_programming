#!/usr/bin/python3
"""
Write a function that prints a square with the character #

"""

def print_square(size):
    """
    Print a square with the character '#' of the given size.

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size <= 0:
        raise ValueError("size must be a positive integer")

    for i in range(size):
        print("#" * size)
