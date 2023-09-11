#!/usr/bin/python3
"""
This module contains a function that returns true if the object is an instance
of a class that inherited directly/indirectly from the specified class
"""


def inherits_from(obj, a_class):
    """Function that checks if object is an instance of a class that inherited
    directly/indirectly from the speecified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
