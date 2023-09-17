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
