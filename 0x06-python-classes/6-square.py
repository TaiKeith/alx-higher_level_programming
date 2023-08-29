#!/usr/bin/python3

"""Create a class Square"""


class Square:
    """class Square that has private instance attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """
        size - A private instance attribute
        position - A private instance attribute
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Property of the coordinates of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value


    def area(self):
        """
        Calculates the area of the square
        Returns: The current square area
        """

        return self.__size ** 2

    def pos_print(self):
        pos = ""
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            pos += "\n"
        for _ in range(self.size):
            pos += " " * self.position[0] + "#" * self.size + "\n"
        return pos

    def __str__(self):
        return self.pos_print()

    def my_print(self):
        """Prints the square in the desired position"""

        print(self.pos_print(), end='')
