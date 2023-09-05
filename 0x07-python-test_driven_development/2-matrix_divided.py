#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a maatrix"""
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list):
        raise TypeError(matrix_msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(matrix_msg)

    row_size = len(matrix[0])
    if not all(len(row == row_size for row in matrix)):
        raise ValueError(matrix_size)

    for row in matrix:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(matrix_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
