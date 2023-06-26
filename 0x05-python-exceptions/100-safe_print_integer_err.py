#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    is_integer = True

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ve:
        is_integer = False
        stderr.write("Exception: {}\n".format(ve))

    return (is_integer)
