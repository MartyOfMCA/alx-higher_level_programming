#!/usr/bin/python3
"""
Return the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returnns a list of available attributes and methods
    for a given object

    Parameters
    obj : object
        The given object

    Return
        A list of defined attributes
    """
    return (dir(obj))
