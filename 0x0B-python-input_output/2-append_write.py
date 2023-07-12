#!/usr/bin/python3
"""
Defines a function that appends a string to the
end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends ``text`` to end of file pointed to by
    ``filename``.

    Parameters
    filename : string, optional
        The full path to the file. Default value is
        empty string
    text : string, optional. Default value is
        empty string

    Return : The total number of characters appened
    """
    chars_appended = 0

    with (open(filename, "a", encoding="utf-8")) as file:
        chars_appended = file.write(text)

    return (chars_appended)
