#!/usr/bin/python3
"""Prints MyList class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
