#!/usr/bin/python3
"""
This module defines the matrix_divided function
# Test for a valid matrix and valid divisor
>>> matrix_divided([
... [1, 2, 3],
... [4, 5, 6],
... [7, 8, 9]
... ], 1)
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

# Test for a valid matrix with divisor set to None
>>> matrix_divided([
... [1, 2, 3],
... [4, 5, 6],
... [7, 8, 9]
... ], None)
Traceback (most recent call last):
...
TypeError: div must be a number

# Test for a matrix of None with a valid divisor
>>> matrix_divided(None, 5)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test for a matrix  of None with a divisor of None
>>> matrix_divided(None, None)
Traceback (most recent call last):
...
TypeError: matrix must be a matrix (list of lists) of integers/floats
"""


def matrix_divided(matrix=[[]], div=1):
    """
    Divides all the elements of the given matrix
    by a dividend.

    Parameters
    matrix : list, optional
        A list composed of a list of integres or floats
        with even number of columns for each row. The
        default value is [[0]].
    div : interger / float, optional
        The number to be used in dividing elements in
        matrix. The default value is 0.

    Raises
    TypeError
        When the given matrix is not a list of list of
        integers or floats. Or when matrix is not
        having the same number of elements (columns) in
        a row. And lastly, when the dividend is not an
        integer or a float
    ZeroDivisionError
        When the dividend is 0

    Return : A list of list of floats with all elements in
    matrix divided by dividend
    """

    new_matrix, row_matrix = [], []
    cell = 0.0
    row, col, col_count = 0, 0, 0
    message = ""

    if (type(matrix) is not list or type(matrix[0]) is not list):
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)

    if (type(div) not in (int, float)):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    col_count = len(matrix[0])
    for row in range(0, len(matrix), 1):
        if (len(matrix[row]) != col_count):
            raise TypeError("Each row of the matrix must have the same size")
        row_matrix = []
        for col in range(0, col_count, 1):
            if (type(matrix[row][col]) not in (int, float)):
                message = "matrix must be a matrix (list of lists) of"
                raise TypeError("{} integers/floats".format(message))
            cell = matrix[row][col] / div
            row_matrix.append(round(cell, 2))
        new_matrix.append(row_matrix)

    return (new_matrix)
