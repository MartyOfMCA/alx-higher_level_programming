#!/usr/bin/python3
"""
Defines a function that writes a string to a
text file
"""


def write_file(filename="", text=""):
    """
    Writes ``text`` to the file pointed to by
    ``filename``.

    Parameters
    filename : string, optional
        The full path to the file. Default value is
        empty string
    text : string, optional. Default value is
        empty string

    Return : The total number of characters written
    """
    chars_written = 0

    with (open(filename, "w", encoding="utf-8")) as file:
        chars_written = file.write(text)

    return (chars_written)
