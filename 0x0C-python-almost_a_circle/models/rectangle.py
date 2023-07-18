#!/usr/bin/python3
""" This module defines the Rectangle class """
from .base import Base


class Rectangle(Base):
    """ Represent the rectangle shape """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of rectangle

        Parameters
        width : integer
            The width for the rectangle
        height : integer
            The height for the rectangle
        x : integer, optional
            The x axis for displaying the rectangle
        y : interger, optional
            The y axis for displaying the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_attribute(self, name, value):
        """
        Validate the given attribute.

        Parameters
        name : string
            The name for the instance attribute to validate
        value : integer
            The value for the instance attribute

        Raises
        TypeError
            When the given value is not an integer
        ValueError
            When the value given is 0 or less and the name
            is width or height. And also when the given
            value is a negative value and the name is x or y.
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (name in ("width", "height")):
            if (value <= 0):
                raise ValueError("{} must be > 0".format(name))
        elif (name in ("x", "y")):
            if (value < 0):
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ Return the width for the rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set the width for the rectangle

        Parameters
        value : integer
            The width for the rectangle
        """
        self.validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """ Return the height for the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height for the rectangle

        Parameters
        value : integer
            The width for the rectangle
        """
        self.validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """ Return the x axis for the rectangle """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set the x axis for the rectangle

        Parameters
        value : integer
            The x axis for the rectangle
        """
        self.validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """ Return the y axis for the rectangle """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set the y axis for the rectangle

        Parameters
        value : integer
            The y axis for the rectangle
        """
        self.validate_attribute("y", value)
        self.__y = value

    def area(self):
        """ Return the area for the rectangle """
        return (self.width * self.height)

    def display(self):
        """
        Print the rectangle
        Return : The number of points printed for the shape.
        """
        points = 0

        for increment in range(0, self.y, 1):
            points += 1
            print()

        for row in range(0, self.height, 1):
            for increment in range(0, self.x, 1):
                points += 1
                print(" ", end="")
            for col in range(0, self.width, 1):
                points += 1
                print("#", end="")
            print()

        return (points)

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        Update the rectangle attributes

        Parameters
        args : tuple
            Values for rectangle attributes as positional
            arguments.
        kwargs : dictionary
            Values for retangle attributes as named
            arguments.
        """
        if (len(args) > 0 and type(args[0]) is int):
            if (len(args) == 1):
                self.id, = args
            elif (len(args) == 2):
                self.id, self.width = args
            elif (len(args) == 3):
                self.id, self.width, self.height = args
            elif (len(args) == 4):
                self.id, self.width, self.height, self.x = args
            else:
                self.id, self.width, self.height, self.x, self.y = args
        else:
            self.id = kwargs.get("id") if kwargs.get("id") is not None \
                else self.id
            self.width = kwargs.get("width") if kwargs.get("width") is \
                not None else self.width
            self.height = kwargs.get("height") if kwargs.get("height") \
                is not None else self.height
            self.x = kwargs.get("x") if kwargs.get("x") is not None \
                else self.x
            self.y = kwargs.get("y") if kwargs.get("y") is not None \
                else self.y

    def to_dictionary(self):
        """
        Returns dictionary representation for instance
        of a rectangle.
        """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "width": self.width, "height": self.height
        }
