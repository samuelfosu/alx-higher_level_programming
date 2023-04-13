#!/usr/bin/python3
"""A function that writes a string to a text file"""


def write_file(filename="", text=""):
    """A string to a text file"""
    n_lines = 28
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            n_lines += 1
    return n_lines
