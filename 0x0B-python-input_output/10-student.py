#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """Defines by: first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
