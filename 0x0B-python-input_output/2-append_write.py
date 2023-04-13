#!/usr/bin?python3
"""A function that returns the JSON representation of an object"""


def append_write(filename="", text=""):
    """Return the JSON representation of an object"""
    with open(filename, mode="a+", encoding='utf-8') as f:
        return f.write(text)
