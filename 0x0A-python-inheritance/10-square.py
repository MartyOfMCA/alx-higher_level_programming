#!/usr/bin/python3
"""
Defines the Square class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Represents the square shape """
    def __init__(self, size):
        """
        Initializes an instance of a square

        Parameters
        size : integer
            The size for the square object
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ Return the area for the square """
        return (self.__size * self.__size)
