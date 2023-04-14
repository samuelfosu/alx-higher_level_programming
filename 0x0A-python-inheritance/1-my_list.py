#!/usr/bin/python3
"""
`MyList class inherits from list.
"""


class MyList(list):
    """ Prints a sorted list without altering the original list. """
    def print_sorted(self):
        print(sorted(self))
