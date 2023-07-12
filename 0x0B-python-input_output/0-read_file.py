#!/usr/bin/python3
""" Defines a function to read a text file """


def read_file(filename=""):
    """
    Read contents from a file to standard output

    Parameters
    filename : string, optional
        The full path to the file. Default value is
        empty string
    """
    with (open(filename, "r", encoding="utf-8")) as file:
        print(file.read(), end="")
