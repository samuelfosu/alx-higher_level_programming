#!/usr/bin/python3
# 2-safe_print_list_integers.py

def safe_print_list_integers(my_list=[], x=0):
    """ Prints x elements of a list and only integers.
    Args:
    my_list - list to be printed from.
    x - number of elements to print
    Returns:
    number of integers printed
    """
    rl_nums = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            rl_nums += 1
        except (ValueError, TypeError):
            pass
    print("")
    return (rl_nums)
