#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Defines a student by: first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""
        return self.__dict__
