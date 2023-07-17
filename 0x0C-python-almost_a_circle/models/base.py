#!/usr/bin/python3
""" This module defines the Base class """


class Base:
    """
    The Base class for shapes

    __nb_objects : integer
        The number of instances created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the class

        id : integer, optional
            The id for the instance created. The default
            value of None is specified if no id is given.
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
