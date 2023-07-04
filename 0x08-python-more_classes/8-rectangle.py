#!/usr/bin/python3

""" Define a class for the rectangle shape """


class Rectangle:

    """
    Represents a rectangular shape
    number_of_instances : int
        The total number of rectanglular instances created
    print_sybmol : any
        The symbol used to draw the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """ Destroy an instance of a rectangle """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """ Returns the area for a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Returns the perimeter for a rectangle
        When either the height or width is 0 returns 0
        """
        perimeter = None

        perimeter = (2 * (self.__width + self.__height))
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0

        return (perimeter)

    def __str__(self):
        """ Returns a string representation for a rectangle """
        obj_str = ""

        if (self.__width == 0 or self.__height == 0):
            return (obj_str)
        for row in range(0, self.__height, 1):
            for col in range(0, self.__width, 1):
                obj_str += str(self.print_symbol)
            if ((row == self.__height - 1) and (col == self.__width - 1)):
                break
            obj_str += "\n"

        return (obj_str)

    def __repr__(self):
        """ Returns a string that can be evaluated to a rectangle """

        return (f"Rectangle({self.__width}, {self.__height})")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two instances of a rectangle and
        return the instance with the biggest area

        Parameters
        rect_1 : Rectangle
            The first rectangle instance
        rect_2 : Rectangle
            The second rectangle instance

        Raises
        TypeError
            When either given instances are not
            of type Rectangle.
        """

        if (type(rect_1) is Rectangle):
            if (type(rect_2) is Rectangle):
                if (rect_1.area() >= rect_2.area()):
                    return rect_1
                return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
