#!/usr/bin/python3
""" Define a custom class that inherits from int """


class MyInt(int):
    """ Custom int class """
    def __eq__(self, other_obj):
        """
        Checks whether the current object value is
        not equal the value of ``other_obj``

        Parameters
        other_obj : MyInt, int
            The second object to compare with
        """
        return (self.real != other_obj.real)

    def __ne__(self, other_obj):
        """
        Checks whether the current object value is
        equal the value of ``other_obj``

        Parameters
        other_obj : MyInt, int
            The second object to compare with
        """
        return (self.real == other_obj.real)
