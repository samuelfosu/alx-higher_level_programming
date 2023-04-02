#!/usr/bin/python3
"""

This function divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    """
    
    Divides the integers or floats in a matrix by a given divisor.

    Args:
        matrix (list of lists of ints/floats): The input matrix.
        div (int or float): The divisor to divide the elements of the matrix by.

    Returns:
        list of lists of floats: A new matrix with the result of the division.

    Raises:
        TypeError: If the input matrix is not a list of lists of ints/floats,
                   or if the divisor is not an int or float.
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the rows of the input matrix are not of equal length,
                   or if any element of the matrix is not an int or float.

    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg_type = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)

    len_e = 0
    msg_size = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_type)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(msg_size)

        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)

        len_e = len(elems)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)
