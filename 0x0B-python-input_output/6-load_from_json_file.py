#!/usr/bin/python3
"""
Defines a function that decodes JSON string
into appropriate object.
"""
import json


def load_from_json_file(filename):
    """
    Decode JSON string into appropriate object.

    Parameters
    filename : string
        The full path to the file.

    Return : The decoded JSON object.
    """
    obj = None

    with open(filename, "r", encoding="utf-8") as file:
        obj = json.loads(file.read())

    return (obj)
