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

    def __lt__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison < check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is less than @other_square_object.
        Otherwise it returns False
        """

        is_less = False

        if (self.area() < other_square_object.area()):
            is_less = True

        return (is_less)

    def __le__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison <= check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is either less than or equals @other_square_object.
        Otherwise it returns False
        """

        is_less_or_equal = False

        if (self.area() <= other_square_object.area()):
            is_less_or_equal = True

        return (is_less_or_equal)

    def __eq__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison == check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is the same as the area of @other_square_object.
        Otherwise it returns False
        """

        is_same = False

        if (self.area() == other_square_object.area()):
            is_same = True

        return (is_same)

    def __ne__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison != check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is different from the area of @other_square_object.
        Otherwise it returns False
        """

        is_not_same = False

        if (self.area() != other_square_object.area()):
            is_not_same = True

        return (is_not_same)

    def __gt__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison > check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is greater than @other_square_object.
        Otherwise it returns False
        """

        is_greater = False

        if (self.area() > other_square_object.area()):
            is_greater = True

        return (is_greater)

    def __ge__(self, other_square_object):
        """
        Compares two Square object based on their area.
        Performs the comparison >= check on the current
        object and another object passed.

        Parameters
        other_square_object : Square
            The second Square object to compare with

        Returns : True if the current (first) object
        area is either greater than or equals @other_square_object.
        Otherwise it returns False
        """

        is_greater_or_equal = False

        if (self.area() >= other_square_object.area()):
            is_greater_or_equal = True

        return (is_greater_or_equal)
