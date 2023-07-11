#!/usr/bin/python3
"""
Defines the BaseGeometry class
"""


class BaseGeometry:
    """
    The Geometry class
    """
    def area(self):
        """
        Returns the area for the geometry object.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name="", value=0):
        """
        Checks and validates ``value``

        Parameters
        name : string
            The name for the value to validate
        value : int
            The value to validate
        """
        if (not isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
