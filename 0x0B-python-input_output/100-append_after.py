#!/usr/bin/python3
""" This module defines the ``append_after`` function """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing
    specific strings in a file.

    Parameters
    filename : string, optional
        The full path to the file.
    search_string : string, optional
        The lookup string. Has a default value of an
        empty string.
    new_string : string, optional
        The new string to insert. Has the default value
        of an empty string.
    """
    words = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            words += line
            if (search_string in line):
                words += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(words)
