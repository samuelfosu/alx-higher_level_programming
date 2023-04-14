#!/usr/bin/python3
"""MyInt class"""


class MyInt(int):
    """Class MyInt inheriting from int"""
    def __eq__(self, other):
        """Inverts =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts !="""
        return super().__eq__(other)
