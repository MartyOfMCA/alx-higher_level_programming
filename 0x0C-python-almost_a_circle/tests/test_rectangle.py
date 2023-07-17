#!/usr/bin/python3
""" This module defines a test class for the Rectangle class """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_width_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(10, rect.width)

    def test_height_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(5, rect.height)

    def test_x_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(1, rect.x)

    def test_y_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(1, rect.y)

    def test_id_from_valid_values_with_id(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(10, rect.id)

    def test_width_from_invalid_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("10", 5, 1, 1, 10)

    def test_height_from_invalid_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, "5", 1, 1, 10)

    def test_x_from_invalid_x(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 5, "1", 1, 10)

    def test_y_from_invalid_y(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 5, 1, "1", 10)

    def test_id_without_obj_id(self):
        rect = Rectangle(10, 5, 1, 1)
        self.assertEqual(6, rect.id)

    def test_width_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 5, 1, 1, 10)

    def test_height_from_negative_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0, 1, 1, 10)

    def test_x_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 5, -1, 1, 10)

    def test_y_from_invalid_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(10, 5, 1, -1, 10)

    def test_one_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(10)

    def test_no_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            rect = Rectangle()
