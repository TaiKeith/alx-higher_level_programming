#!/usr/bin/python3
"""
This module appends a string to a text file & returns the number of
characters written
"""


def append_write(filename="", text=""):
    """A function that appends a string to a text file

    filename:
    The name of the file

    text:
    The string to be appended

    Return:
    The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
