#!/usr/bin/python3
""" This module defines a test class for the Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_single_obj_with_id(self):
        base = Base(10)
        self.assertEqual(10, base.id)

    def test_single_obj_without_id(self):
        base = Base()
        self.assertEqual(1, base.id)

    def test_two_obj_with_id(self):
        base = Base(10)
        base2 = Base(5)
        self.assertEqual(5, base2.id)

    def test_two_obj_with_first_id(self):
        base = Base(5)
        base2 = Base()
        self.assertEqual(2, base2.id)

    def test_two_obj_with_second_id(self):
        base = Base()
        base2 = Base(3)
        self.assertEqual(3, base2.id)

    def test_two_obj_without_ids(self):
        base = Base()
        base2 = Base()
        self.assertEqual(5, base2.id)

    def test_single_obj_with_neg_id(self):
        base = Base(-5)
        self.assertEqual(-5, base.id)

    def test_two_obj_with_neg_ids(self):
        base = Base(-1)
        base2 = Base(-2)
        self.assertEqual(-2, base2.id)

    def test_to_json_string_with_valid_dictionary(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted('[{"x": 2, "width": 10, "id": 1, "height": 7'
                                ', "y": 8}]'), sorted(json_dictionary))

    def test_to_json_string_with_argument_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual("[]", json_string)

    def test_to_json_string_with_empty_dictionary(self):
        json_string = Base.to_json_string({})
        self.assertEqual("[]", json_string)

    def test_save_to_file_with_two_rectangle_objects(self):
        rect1 = Rectangle(1, 1, 1, 1, 1)
        rect2 = Rectangle(2, 2, 2, 2, 2)
        Rectangle.save_to_file([rect1, rect2])
        actual = Base.file_exists(["Rectangle.json"])
        self.assertTrue(actual)

    def test_save_to_file_with_one_rectangle_object(self):
        rect = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([rect])
        actual = Base.file_exists(["Rectangle.json"])
        self.assertTrue(actual)

    def test_save_to_file_with_two_square_objects(self):
        square1 = Square(1, 1, 1, 1)
        square2 = Square(2, 2, 2, 2)
        Square.save_to_file([square1, square2])
        actual = Base.file_exists(["Square.json"])
        self.assertTrue(actual)

    def test_save_to_file_with_one_square_object(self):
        square = Square(1, 1, 1, 1)
        Square.save_to_file([square])
        actual = Base.file_exists(["Square.json"])
        self.assertTrue(actual)
