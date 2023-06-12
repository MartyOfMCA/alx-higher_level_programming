#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    dup_list = my_list.copy()
    if (idx < 0):
        return (dup_list)
    if (idx > len(my_list) - 1):
        return (dup_list)
    dup_list[idx] = element
    return (dup_list)
