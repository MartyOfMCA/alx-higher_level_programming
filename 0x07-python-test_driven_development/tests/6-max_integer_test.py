#!/usr/bin/python3
"""
This module defines a test class to perform
unit test on a function
"""
import unittest


class TestMaxInteger(unittest.TestCase):

    __max_integer = None

    def setUp(self):
        self.__max_integer = __import__("6-max_integer").max_integer

    def test_empty_list(self):
        self.assertEqual(self.__max_integer([]), None)

    def test_unique_list(self):
        self.assertEqual(self.__max_integer([1, 2, 3, 4, 5]), 5)

    def test_same_items_in_list(self):
        self.assertEqual(self.__max_integer([2, 2, 2, 2]), 2)

    def test_single_item_in_list(self):
        self.assertEqual(self.__max_integer([990]), 990)

    def test_similar_items_in_list(self):
        self.assertEqual(self.__max_integer([2, 8, 2, 2]), 8)

    def test_strings_as_list(self):
        self.assertEqual(self.__max_integer("abc"), "c")

    def test_max_integer_no_argument(self):
        self.assertEqual(self.__max_integer(), None)

    def test_empty_collection(self):
        with self.assertRaises(TypeError):
            self.__max_integer(20)
            self.__max_integer(7.9)

    def test_first_item_is_max(self):
        self.assertEqual(self.__max_integer([8, 2, 1]), 8)
