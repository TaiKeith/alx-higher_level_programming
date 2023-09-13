#!/usr/bin/python3
"""
This module writes a string to a text file & returns the number of
characters written
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file

    filename:
    The name of the file

    text:
    The string to be written

    Return:
    The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
