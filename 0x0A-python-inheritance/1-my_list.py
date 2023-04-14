#!/usr/bin/python3
class MyList(list):
    """ Class that inherits the attributes references """
    def print_sorted(self):
        print(sorted(self))
