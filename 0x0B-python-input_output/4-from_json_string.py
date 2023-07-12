#!/usr/bin/python3
"""
Defines a function that returns an object from a
JSON string.
"""
import json


def from_json_string(my_str):
    """
    Decodes the given JSON string to an object.

    Parameters
    my_str : string
        The string to be decoded

    Return : An object from ``my_str``
    """
    return (json.loads(my_str))
