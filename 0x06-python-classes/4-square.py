#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """
    class Square that has a private attribute size
    and checks if size is an integer
    """

    def __init__(self, size=0):
        """size - A private attribute instance"""

        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Modifies the attribute value"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns: The current square area
        """

        return self.__size ** 2
