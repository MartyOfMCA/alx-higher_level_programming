#!/usr/bin/python3
"""
This module contains functions to find the
peak in a list of integers.
"""


def find_peak(list_of_integers):
    """
    Find the peak in the given list.

    Parameters
    list_of_integers : list
        A list of integers

    Return
        The peak value
    """
    if (not list_of_integers):
        return None
    size = len(list_of_integers)

    return (list_of_integers[find_peak_index(list_of_integers, size // 2)])


def find_peak_index(list_of_integers, midpoint_index):
    """
    Returns the index for the peak item
    in the given list.

    Parameters
    list_of_integers : list
        The list to search.
    midpoint_index : integer
        The midpoint in the given list

    Return
        The index of the midpoint item.
    """

    left_value = list_of_integers[midpoint_index - 1]
    midpoint_value = list_of_integers[midpoint_index]
    right_value = list_of_integers[midpoint_index + 1]

    if (midpoint_value >= left_value and midpoint_value >= right_value):
        return (midpoint_index)

    if (midpoint_index > 1):
        return (find_peak_index(list_of_integers, midpoint_index // 2))
    return (find_peak_index(list_of_integers, (len(list_of_integers) +
            midpoint_index + 1) // 2))
