#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""
    pos = -1

    for letter in str:
        pos += 1
        if (pos == n):
            continue
        new_str += letter
    return new_str
