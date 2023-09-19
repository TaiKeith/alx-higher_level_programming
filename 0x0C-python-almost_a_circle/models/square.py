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

    def update(self, *args, **kwargs):
        """
        Public method that assigns an argument to each attribute
        If *args exists and is not empty, it assigns positional arguments
        in the order:
        args:
            variable-length argument list (id, width, height, x, y)

        If **kwargs exists, it assigns key/value arrguments to the
        attributes
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of
        a Square
        """
        attributes = ["id", "size", "x", "y"]
        return {attr: getattr(self, attr) for attr in attributes}
