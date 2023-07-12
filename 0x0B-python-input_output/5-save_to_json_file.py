#!/usr/bin/python3
"""
Defines a function that writes writes encoded
object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write encoded string for given object to the
    given file.

    Parameters
    my_obj : object
        The object to encode
    filename : string
        The full path to the file.
    """
    obj_str = ""

    with open(filename, "w", encoding="utf-8") as file:
        obj_str = json.dumps(my_obj)
        file.write(obj_str)
