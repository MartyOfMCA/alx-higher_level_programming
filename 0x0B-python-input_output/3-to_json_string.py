#!/usr/bin/python3
"""
Defines a function that returns the JSON
representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Encodes the given object to a JSON string

    Parameters
    my_obj : object
        The object to be encoded

    Return : A string representation for ``my_obj``
    """
    return (json.dumps(my_obj))
