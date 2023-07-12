#!/usr/bin/python3
"""
This module defines a function that returns
pascal traingle
"""


def pascal_triangle(n):
    """
    Returns a list of intergers representing the
    Pascal triangle for the given number.

    Parameters
    n : integer
        The rows in the triangle

    Return : A list of list of integers representing
    Pascal's triangle.
    """
    my_list = []
    top_left = 1
    top_right = 1

    if (n <= 0):
        return my_list

    """
    Populate Pascal triangle with rows and columns
    in the triangle filled with the number 1
    """
    for increment in range(0, n, 1):
        my_list.append([1] * (increment + 1))

    for row in range(2, n, 1):
        for col in range(1, row, 1):
            top_left = my_list[row - 1][col - 1]
            top_right = my_list[row - 1][col]
            my_list[row][col] = top_left + top_right

    return (my_list)
