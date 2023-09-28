#!/usr/bin/python3
# Comment goes here

def find_peak(list_of_integers):
    """
    Finds the peak in the given list.

    Parameters
    list_of_integers : list
        A list of integers

    Return
        The peak value
    """
    if (list_of_integers == []):
        return (None)

    return (sorted(list_of_integers)[-1])
