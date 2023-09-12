#!/usr/bin/python3
"""This module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2
