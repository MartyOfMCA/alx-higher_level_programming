#!/usr/bin/python3
""" This module defines a test class for the Square class """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_width_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.width)

    def test_height_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.height)

    def test_x_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(1, square.x)

    def test_y_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(1, square.y)

    def test_id_from_valid_values_with_id(self):
        square = Square(10, 1, 1, 10)
        self.assertEqual(10, square.id)

    def test_width_from_invalid_type(self):
        with self.assertRaises(TypeError):
            Square("10", 1, 1, 10)
    
    def test_x_from_invalid_x(self):
        with self.assertRaises(TypeError):
            Square(10, "1", 1, 10)

    def test_y_from_invalid_y(self):
        with self.assertRaises(TypeError):
            Square(10, 1, "1", 10)

    def test_id_without_obj_id(self):
        square = Square(10, 1, 1)
        self.assertEqual(21, square.id)

    def test_id_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(-10, 1, 1, 10)

    def test_width_from_negative_value(self):
        with self.assertRaises(ValueError):
            Square(0, 1, 1, 10)

    def test_x_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(10, -1, 1, 10)

    def test_y_from_invalid_value(self):
        with self.assertRaises(ValueError):
            Square(10, 1, -1, 10)

    def test_height_one_positional_arg_provided(self):
        square = Square(10)
        self.assertEqual(10, square.height)

    def test_no_positional_arg_provided(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.size)

    def test_width_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.width)

    def test_height_attribute_with_valid_size(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(10, square.height)

    def test_size_attribute_with_invalid_size_type(self):
        with self.assertRaises(TypeError):
            square = Square(5)
            square.size = "10"

    def test_size_attribute_with_invalid_size_value(self):
        with self.assertRaises(ValueError):
            square = Square(5)
            square.size = 0
