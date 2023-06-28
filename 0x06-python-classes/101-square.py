#!/usr/bin/python3

"""
Define a module for the Square shape
"""


class Square:
    """
    Define the Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize an instance of the Square class

        Parameters
        size : int, optional
            The size of the square (default is 0)
        position : tuple, optional
            The position for the squsre
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Returns : The size for a square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size for a square

        Parameters
        value : int
            The size of the square

        Raises
        TypeError
            If the size passed is not an integer
        ValueError
            If the size passed is a negative number

        Returns : None
        """

        if (type(value) is int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Return the position for a square
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of a square

        Parameters
        value : tuple
            The position of the square

        Raises
        TypeError
            If the position is not a tuple of 2
            positive integers
        """

        if (type(value) is not tuple or
           type(value) is tuple):
            if (len(value) != 2 or
               type(value[0]) is not int or
               type(value[1]) is not int or
               value[0] < 0 or value[1] < 0):
                raise TypeError(
                        "position must be a tuple of 2 positive integers")
            else:
                self.__position = value

    def area(self):
        """
        Returns : The area for the square
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square using the # character
        """

        row, col, increment = 0, 0, 0

        if (self.__size == 0):
            print()
            return (None)

        for increment in range(0, self.__position[1], 1):
            print()
        for row in range(0, self.__size, 1):
            for col in range(0, (self.__size + self.position[0]), 1):
                if (col < self.position[0]):
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """
        The string representation for a square
        """

        text = ""

        row, col, increment = 0, 0, 0
        if (self.__size == 0):
            return (text)

        for increment in range(0, self.__position[1], 1):
            text += "\n"
        for row in range(0, self.__size, 1):
            for col in range(0, (self.__size + self.position[0]), 1):
                if (col < self.position[0]):
                    text += " "
                    continue
                text += "#"
            text += "\n"

        return (text[0:-1])
