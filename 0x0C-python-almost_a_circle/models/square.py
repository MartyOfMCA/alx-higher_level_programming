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

    def update(self, *args, **kwargs):
        """
        Update the square attributes

        Parameters
        args : tuple
            Values for square attributes as positional
            arguments.
        kwargs : dictionary
            Values for square attributes as named
            arguments.
        """
        if (len(args) > 0 and type(args[0]) is int):
            if (len(args) == 1):
                self.id, = args
            elif (len(args) == 2):
                self.id, self.size = args
            elif (len(args) == 3):
                self.id, self.size, self.x = args
            else:
                self.id, self.size, self.x, self.y = args
        else:
            self.id = kwargs.get("id") if kwargs.get("id") is not None \
                else self.id
            self.size = kwargs.get("size") if kwargs.get("size") is \
                not None else self.size
            self.x = kwargs.get("x") if kwargs.get("x") is not None \
                else self.x
            self.y = kwargs.get("y") if kwargs.get("y") is not None \
                else self.y
