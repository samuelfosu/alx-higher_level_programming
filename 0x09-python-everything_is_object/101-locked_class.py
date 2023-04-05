#!/usr/bin/python3
"""Locked class"""


class LockedClass:
    """
    Prevent the user from instantiating any new LockedClass attribute but 'first_name'.
    """
    __slots__ = ["first_name"]

