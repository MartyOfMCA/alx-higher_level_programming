#!/usr/bin/python3
"""
This module defines the print_square function
# Test for a valid size
>>> print_square(5)
#####
#####
#####
#####
#####
"""


def print_square(size=0):
    """
    Prints a square from the given size

    Parameters
    size : int / float

    Raises
    TypeError
        When the size is not a number or a floating
        point value with a value less than 0
    ValueError
        When the size is given as an integer but with
        a value less than 0
    """

    conv = size
    row, col = 0, 0

    if (size == 0):
        return (None)
    if (type(size) not in (float, int)):
        raise TypeError("size must be an integer")
    if (type(size) is float):
        if (size < 0):
            raise TypeError("size must be an integer")
        conv = int(size)
    if (size < 0):
        raise ValueError("size must be >= 0")

    for row in range(0, conv, 1):
        for col in range(0, conv, 1):
            print("#", end="")
        print()
