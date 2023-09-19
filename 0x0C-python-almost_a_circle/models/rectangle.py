#!/usr/bin/python3
"""
This module contains class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle and inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor for Rectangle

        Args:
            width (int): Private attribute for the width of the Rectangle
            height (int): Private attribute for the height of the Rectangle
            x (int): Private attribute for x value of the Rectangle
            y (int): Private attribute for y value of the Rectangle
            id (int): Private attribute id inherits from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Property method for width value

        Return:
            __width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width value

        Arg:
            value (int): Value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Property method for height value

        Return:
            __height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height value

        Arg:
            value (int): Value to be set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Property method for x value
        Return:
            __x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x value
        Arg:
            value (int): Value to be set
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Property method for y value
        Return:
            __y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y value
        Arg:
            value (int): Value to be set
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        Public method for Rectangle
        Return:
            Area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        Public method for Rectangle that prints out the Rectangle instance
        with the character '#'
        """
        rectangle = ""
        print_symbol = "#"

#        for i in range(self.__height):
#            rectangle += print_symbol * self.__width + "\n"
#        print(rectangle, end="")
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            rectangle += (" " * self.x) + (print_symbol * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """Returns a string format of the Rectangle instance"""
        return (
                f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}"
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
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of
        a Rectangle
        """
        attributes = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attributes}
