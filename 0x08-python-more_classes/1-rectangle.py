#!/usr/bin/python3

""" Define a class for the rectangle shape """


class Rectangle:
    """ Represents a rectangular shape """

    def __init__(self, width=0, height=0):
        """
        Initialize an instance for a rectangle

        Parameters
        width : integer, optional
            The width for the rectangle. By default its set to 0
        height : integer, optional
            The height for the rectangle. By defaqult its set to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ To obtain the width for a rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width for a rectangle

        Parameters
        value : integer
            The value for the rectangle's width

        Raises
        TypeError
            When value is any type other than an integer
        ValueError
            When the value is any integer less than 0
        """
        if (type(value) is int):
            if (value >= 0):
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ To obtain the height for a rectangle """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set the height for a rectangle

        Parameters
        value : integer
            The value for the rectangle's height

        Raises
        TypeError
            When value is any type other than an integer
        ValueError
            When the value is any integer less than 0
        """
        if (type(value) is int):
            if (value >= 0):
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
