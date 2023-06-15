#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys = list(key for key, _value in a_dictionary.items() if _value == value)

    for key in keys:
        del(a_dictionary[key])

    return (a_dictionary)
