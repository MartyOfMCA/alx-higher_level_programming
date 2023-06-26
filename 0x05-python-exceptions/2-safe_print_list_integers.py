#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0

    for increment in range(0, x, 1):
        try:
            print("{:d}".format(my_list[increment]), end="")
        except (ValueError, TypeError):
            continue
        elements_printed += 1
    print()

    return (elements_printed)
