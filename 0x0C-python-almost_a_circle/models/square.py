#!/usr/bin/python3
""" This module defines the Square class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Represents the square shape """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance of a square

        Parameters
        size : integer
            The size (width and height) for the square
        x : integer, optional
            The x axis for displaying the square
        y : integer, optional
            The y axis for displaying the square
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width, self.height))

    @property
    def size(self):
        """ Return the size for the square """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Set the size for the square

        Parameters
        value : integer
            The size for the square
        """
        self.width = value
        self.height = value
