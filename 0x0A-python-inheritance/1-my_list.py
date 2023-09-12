#!/usr/bin/python3
"""
This module contains a class that inherits from 'list'
"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
