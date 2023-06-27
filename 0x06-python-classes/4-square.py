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
        """
        self.size = size

    def area(self):
        """
        Retuens the area for a square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """
        Returns the size for a square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of a square

        Parameters
        value : int
            The size of the square

        Raises
        TypeError
            If the size passed is not an integer
        ValueError
            If the size passed is a negative number
        """

        if (type(value) is int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
