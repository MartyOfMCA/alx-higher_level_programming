#!/usr/bin/python3

"""
Define a module for a singly-linked list operations.

This module contains a Node and a singly-linked
list
"""


class Node:
    """
    Define a node that can store data and another Node
    """

    def __init__(self, data, next_node=None):
        """
        Initialize an instance of the Node

        Parameters
        data : int
            The data value for the node
        next_node : Node, optional
            The next node in the list
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Returns the data value for a Node
        """

        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the data value for a Node

        Parameters
        value : int
            The data value for the Node

        Raises
        TypeError
            If the value passed is not an integer
        """

        if (type(value) is int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Returns the next node
        """

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node for a Node

        Parameters
        value : Node or None
            The next node for a Node

        Raises
        TypeError
            If the value passed is neither a Node nor None
        """

        if (type(value) is Node or value is None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    """
    Define a singly-linked list
    """

    def __init__(self):
        """
        Initialize the linked list
        """

        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node in the sorted list using the
        given value

        Parameters
        value : int
        """

        current, previous = None, None
        new_node = Node(value)

        if (self.__head is None):
            self.__head = new_node
            return
        current = self.__head
        while current is not None:
            if (current.data < value):
                previous = current
                current = current.next_node
                continue
            break
        if (previous is not None):
            previous.next_node = new_node
        else:
            self.__head = new_node
        new_node.next_node = current

    def __str__(self):
        """
        String representation for a Node
        """

        current = None
        obj_as_str = ""

        current = self.__head
        while current is not None:
            obj_as_str += str(current.data) + "\n"
            current = current.next_node

        return (obj_as_str[0:-1])
