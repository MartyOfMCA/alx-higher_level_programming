#!/usr/bin/python3
"""
This module defines the say_my_name function
# Test for a valid first and last names
>>> say_my_name("Martin", "Amankwaa")
My name is Martin Amankwaa
"""


def say_my_name(first_name="", last_name=""):
    """
    Prints the full name from the parameters given

    Parameters
    first_name : str, optional
        The first name. Has the default value of an
        empty string
    last_name : str, optional
        The last name. Has the default value of an empty
        string

    Raises
    TypeError
        When either the first or last name given
        is not a string
    """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")
    if (first_name == "" and last_name == ""):
        raise ValueError("No name passed: say_my_name(first_name, last_name)")

    print("My name is {} {}".format(first_name, last_name))
