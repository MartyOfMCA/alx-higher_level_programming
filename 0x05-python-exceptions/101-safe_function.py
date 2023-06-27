#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):
    result = None

    try:
        result = fct(*args)
    except (ZeroDivisionError, IndexError) as exc:
        stderr.write("Exception: {}\n".format(exc))

    return (result)
