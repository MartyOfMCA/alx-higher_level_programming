#!/usr/bin/python3
""" Define a Student class """


class Student:
    """ A classs representing a student instance """
    def __init__(self, first_name, last_name,  age):
        """
        Initialize a student instance.

        Parameters
        first_name : string
            The first name for the student
        last_name : string
            The last name for the student
        age : integer
            The age for the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary of all attributes of
        a student instance
        """
        my_dict = dict()

        if (type(attrs) is not list):
            return (self.__dict__)

        for item in attrs:
            if (item in self.__dict__.keys()):
                my_dict.__setitem__(item, self.__dict__.get(item))

        return (my_dict)
