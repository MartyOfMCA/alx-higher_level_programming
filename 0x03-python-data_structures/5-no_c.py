#!/usr/bin/python3

def no_c(my_string):
    dup_string = ""

    for character in my_string:
        dup_string += ("" if character in "cC" else character)

    return (dup_string)
