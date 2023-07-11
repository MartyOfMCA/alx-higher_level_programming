#!/usr/bin/python3
"""
Module defines a custom List
"""


class MyList(list):
    """
    Create a custom list from the list type
    """

    def print_sorted(self):
        """
        Create a temporary copy of the actual list
        stored in the object and print the elements
        in the sorted increasing order.
        """
        list_clone = self.copy()
        list_clone.sort()
        print(list_clone)
