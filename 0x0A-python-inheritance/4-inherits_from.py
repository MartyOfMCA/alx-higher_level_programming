#!/usr/bin/python3
"""
Module defines a function to determine whether an
object is an instance of the specified class directly
or indirectly
"""


def inherits_from(obj, a_class):
    """
    Determine whether the given object is an
    instance of the given type directly or
    indirectly

    Parameters
    obj : object
        The instance variable
    a_class : type
        The class type to be compared against

    Return : True if ``object`` is either a direct
    instance of ``a_class`` or inherits from  subtypes
    of ``a_class`` otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
