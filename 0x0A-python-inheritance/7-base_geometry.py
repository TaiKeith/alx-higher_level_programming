#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
