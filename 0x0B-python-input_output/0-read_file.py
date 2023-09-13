#!/usr/bin/python3
"""
This module reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """A function that reads a text file and prints it out

    filename:
    The name of the file
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')
