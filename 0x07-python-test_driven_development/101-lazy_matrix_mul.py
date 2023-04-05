#!/usr/bin/python3.5
"""
A function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ This module multiplies 2twomatrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        result of the multiplication
    """

    return (np.matmul(m_a, m_b))
