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

    def test_area(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual(50, rect.area())

    def test_display_nno_padding(self):
        rect = Rectangle(1, 1, 0, 0, 10)
        self.assertEqual(1, rect.display())

    def test_magic_str_with_valid_values(self):
        rect = Rectangle(10, 5, 1, 1, 10)
        self.assertEqual("[Rectangle] (10) 1/1 - 10/5", str(rect))

    def test_magic_str_without_axis_nor_id(self):
        rect = Rectangle(10, 5)
        self.assertEqual("[Rectangle] (7) 0/0 - 10/5", str(rect))

    def test_magic_str_without_id(self):
        rect = Rectangle(10, 5, 1, 1)
        self.assertEqual("[Rectangle] (8) 1/1 - 10/5", str(rect))

    def test_display_with_padding(self):
        rect = Rectangle(1, 1, 1, 1, 10)
        self.assertEqual(3, rect.display())

    def test_update_with_one_arg(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(rect))

    def test_update_with_two_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rect))

    def test_update_with_three_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(rect))

    def test_update_with_four_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(rect))

    def test_update_with_five_args(self):
        rect = Rectangle(10, 10, 10, 10)
        rect.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(rect))
