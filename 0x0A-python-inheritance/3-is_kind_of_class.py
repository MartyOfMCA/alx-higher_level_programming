#!/usr/bin/python3
"""
Module defines a function to determine whether an
object is an instance of the specified class or
any of its subtypes
"""


def is_kind_of_class(obj, a_class):
    """
    Determine whether the given object is an
    instance of the given type or any of base
    class's subtypes

    Parameters
    obj : object
        The instance variable
    a_class : type
        The class type to be compared against

    Return : True if ``object`` is either a direct
    instance of ``a_class`` or inherits from  subtypes
    of ``a_class`` otherwise False.
    """
    return (issubclass(type(obj), a_class))
