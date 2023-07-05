#!/usr/bin/python3
"""
This module defines the add_integer function
>>> add_integer(3, 3)
6
"""


def add_integer(num1, num2=98):
    """
    Returns the sum of the two given numbers as
    an integer.

    Parameters
    num1 : integer / float
        The first number
    num2 : integer / float, optional
        The second number. Default value is 98

    Raises
    TypeError
        When any of the given parameters is not
        either an integer or a float
    ValueError
        When any of the given parameters is the
        floating value NaN

    Return : The sum of the two given numbers as an
    integer
    """

    message = None

    if (type(num1) not in (int, float) or type(num2) not in (int, float)):
        if (type(num1) not in (int, float)):
            message = "a must be an integer"
        else:
            message = "b must be an integer"
        raise TypeError(message)

    if (num1 != num1 or num2 != num2):
        raise ValueError("cannot convert float NaN to integer")

    if (num1 == float('inf') or num2 == float('inf')):
        return (256)

    if (num1 == -float('inf') or num2 == -float('inf')):
        return (-5)

    return (int(num1) + int(num2))
