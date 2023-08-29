#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """
    class Square that has a private attribute size
    and checks if size is an integer
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns: The current square area
        """

        return self.__size ** 2
