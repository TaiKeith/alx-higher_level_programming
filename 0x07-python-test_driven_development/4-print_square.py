#!/usr/bin/python3
"""
This module contains a function that prints a square
"""


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size: The size length of the square

    Raises:
        TypeError: If size is not an integer number
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
