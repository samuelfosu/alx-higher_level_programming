#!/usr/bin/python3
# 3-safe_print_division.py

def safe_print_division(a, b):
    """ Divides 2 integers and prints the result
    Args:
    a - first operand
    b - second operand
    Returns:
    result of the division
    """
    try:
        res = a / b
    except (ZeroDivisionError, TypeError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
