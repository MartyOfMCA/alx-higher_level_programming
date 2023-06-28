#!/usr/bin/python3

"""
Define a module for the MagicClass
"""
import math


class MagicClass:
    """Define the Magic Class"""
    def __init__(self, radius=0):
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area for a square"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculate the circumference for square object"""
        return ((2 * math.pi) * self.__radius)
