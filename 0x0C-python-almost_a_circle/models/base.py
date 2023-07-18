#!/usr/bin/python3
""" This module defines the Base class """
import json
from os.path import isfile


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of the
        given arguments to a file.

        Parameters
        list_objs : list
            The list of objects to be encoded to JSON string
        """
        file = None
        file_name = "{}.json".format(cls.__name__)
        obj_dict = {}
        obj_list = []

        if (list_objs is not None):
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                obj_list.append(obj_dict)

        with open(file_name, "w") as file:
            file.write(Base.to_json_string(obj_list))

    @staticmethod
    def file_exists(file_names):
        """
        Determines whether the given file exists

        Parameters
        file_names : list
            A list of file names to be checked

        Return : True when the list of files are valid
        files that exists. Otherwise False.
        """
        for file_name in file_names:
            if (not isfile(file_name)):
                return (False)

        return (True)
