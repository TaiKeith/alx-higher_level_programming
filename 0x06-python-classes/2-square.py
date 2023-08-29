#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """
    class Square that has a private attribute size
    and checks if size is an integer
    """

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
