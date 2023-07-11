#!/usr/bin/python3
"""
Define a function to check whether a new attribute
can be dynamically bound to an object
"""


def add_attribute(obj, name, value):
    """
    Dynamically bind the given attribute name
    along with its value to the given object.

    Parameters
    name : string
        The attribute name
    value : string
        The attribute value
    """
    if (hasattr(obj, "__dict__")):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
