#!/usr/bin/python3
"""
A module that contains a function that returns True if the object is exactly
an instance of the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """Function that checks if object is an instance of specified class"""
    return True if isinstance(obj, a_class) else False
