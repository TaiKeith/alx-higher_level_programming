#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance
of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns true if obj is an instance of a class
    or a class that inherited from the specified class
    """
    return isinstance(obj, a_class)
