#!/usr/bin/python3
"""
This module contains class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square and inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor for Square

        Attribute:
            size (int): The size of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Property method for size
        Return:
            size value
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size value
        Arg:
            value (int): Value to be set
        """

        self.width = value
        self.height = value

    def __str__(self):
        """Overloading str function"""
        return (
                f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
                f"{self.size}"
                )
