#!/usr/bin/python3

def safe_print_integer(value):
    is_valid = True

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        is_valid = False

    return (is_valid)
