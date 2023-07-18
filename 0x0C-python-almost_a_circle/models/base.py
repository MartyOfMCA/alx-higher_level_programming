#!/usr/bin/python3
""" This module defines the Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation for the
        given argument.

        Parameters
        list_arguments : list
            A list of dictionaries
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")

        return (json.dumps(list_dictionaries))
