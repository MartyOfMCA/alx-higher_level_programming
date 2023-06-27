#!/usr/bin/python3

"""
Define a module for the Square shape
"""


class Square:
    """
    Define the Square shape
    """
    def __init__(self, size=0):
        """
        Initializes an instance of the Square class

        Parameters
        size : int, optional
            The size of the square (default is 0)

        Raises
        TypeError
            If the size passed is not an integer
        ValueError
            If the size passed is a negative number
        """

        if (type(size) is int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Returns the area for a square
        """

        return (self.__size ** 2)
