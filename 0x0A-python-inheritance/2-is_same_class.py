#!/usr/bin/python3
"""
Module defines a function to determine whether an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Determine whether the given object is an
    exact instance of the given type

    Parameters
    obj : object
        The instance variable
    a_class : type
        The class type to be compared against

    Return : True if ``object`` is exactly
    an instance of ``a_class`` otherwise False.
    """
    return (type(obj) in (a_class, ))
