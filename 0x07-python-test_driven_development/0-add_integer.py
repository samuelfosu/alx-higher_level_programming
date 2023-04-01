#!/usr/bin/python3
"""
This module defines a function that adds two numbers.
"""

def add_numbers(num1, num2=98):
    """
    This function adds two integer and/or float numbers.

    Args:
        num1: The first number.
        num2: The second number. Defaults to 98.

    Returns:
        The sum of the two given numbers.

    Raises:
        TypeError: If num1 or num2 are not integer or float.
    """

    if not isinstance(num1, (int, float)):
        raise TypeError("num1 must be an integer or float")
    if not isinstance(num2, (int, float)):
        raise TypeError("num2 must be an integer or float")

    num1 = int(num1)
    num2 = int(num2)

    return num1 + num2
