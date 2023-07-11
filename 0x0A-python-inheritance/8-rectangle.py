#!/usr/bin/python3
"""
Defines the Rectangle classes
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents the geometry shape for a rectangle
    """
    def __init__(self, width, height):
        """
        Initializes an instance of a rectangle.

        Parameters
        width : int
            The width for the rectangle
        height : int
            The height for the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
