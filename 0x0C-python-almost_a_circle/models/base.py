#!/usr/bin/python3
""" This module defines the Base class """
import json
import csv
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
            if (len(list_objs) == 0):
                raise ValueError("No instances available")
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                obj_list.append(obj_dict)

        with open(file_name, "w") as file:
            file.write(Base.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts the given string to appropriate object.

        Parameters
        json_string : string
            The JSON string to decode

        Return : The object for the JSON string
        """
        if (json_string is None or json_string == ""):
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance for a class with attributes
        from the specified argument.

        Parameters
        dictionary : dictionary
            Keyword arguments with attributes for the instance
            being created

        Return : An instance for a class with attributes
        """
        instance = None

        if (cls.__name__ == "Rectangle"):
            instance = cls(5, 2)
        else:
            instance = cls(1)
        instance.update(**dictionary)

        return (instance)

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from files """
        file_name, json_string = "", ""
        list_of_instances = []

        file_name = "{}.json".format(cls.__name__)
        if (isfile(file_name)):
            with open(file_name, "r") as file:
                json_string = file.read()
            for instance in Base.from_json_string(json_string):
                list_of_instances.append(cls.create(**instance))

        return (list_of_instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize the given instances into a CSV
        file.

        Parameters
        list_objs : list
            The list of instances to serialize
        """
        file_name = "{}.csv".format(cls.__name__)
        file = None
        obj_attributes = []

        if (list_objs is not None):
            if (len(list_objs) == 0):
                raise ValueError("No instances available")
            with open(file_name, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                for obj in list_objs:
                    obj_attributes.append(obj.id)
                    if (cls.__name__ == "Rectangle"):
                        obj_attributes.append(obj.width)
                        obj_attributes.append(obj.height)
                    else:
                        obj_attributes.append(obj.size)
                    obj_attributes.append(obj.x)
                    obj_attributes.append(obj.y)
                    writer.writerow(obj_attributes)
                    obj_attributes = []

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes CSV file into class instance """
        file_name, csv_string = "", ""
        list_of_instances = []
        obj_dict = {}

        file_name = "{}.csv".format(cls.__name__)
        if (isfile(file_name)):
            with open(file_name, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    obj_dict["id"] = int(row[0])
                    if (cls.__name__ == "Rectangle"):
                        obj_dict["width"] = int(row[1])
                        obj_dict["height"] = int(row[2])
                        obj_dict["x"] = int(row[3])
                        obj_dict["y"] = int(row[4])
                    else:
                        obj_dict["size"] = int(row[1])
                        obj_dict["x"] = int(row[2])
                        obj_dict["y"] = int(row[3])
                    list_of_instances.append(cls.create(**obj_dict))

        return (list_of_instances)
