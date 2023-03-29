#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list.
    Args:
    my_list - list to print from.
    x - number of elements
    Returns:
    number of printed elements.
    """
    num_el = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num_el += 1
        except IndexError:
            break
    print("")
    return (num_el)
