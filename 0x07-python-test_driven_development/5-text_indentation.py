#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after
each of some characters
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':' characters

    Args:
        text: Input string

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = text[:]

    for x in ".?:":
        list_text = t.split(x)
        t = ""
        for i in list_text:
            i = i.strip(" ")
            t = i + x if t is "" else t + "\n\n" + i + x

    print(t[:-3], end="")
