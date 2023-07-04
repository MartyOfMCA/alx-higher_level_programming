#!/usr/bin/python3
""" Define a class called LockedClass """


class LockedClass:
    """
    Prevent users from dynamically binding any
    attribute other than first_name
    """
    __slots__ = ["first_name"]
