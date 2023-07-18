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

    def test_from_json_string_from_valid_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_str = Rectangle.to_json_string(list_input)
        output = Rectangle.from_json_string(json_str)
        self.assertEqual(list_input, output)

    def test_from_json_string_from_none(self):
        output = Rectangle.from_json_string(None)
        self.assertEqual([], output)

    def test_from_json_string_from_empty(self):
        output = Rectangle.from_json_string("")
        self.assertEqual([], output)

    def test_save_to_file_with_two_rectangle_objects_two(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 1, 1, 2)
        file_contents = ""
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            file_contents = file.read()
        self.assertEqual(sorted('[{"y": 8, "x": 2, "id": 1, "width": 10, '
                                '"height": 7}, {"y": 1, "x": 1, "id": 2, '
                                '"width": 2, "height": 4}]'),
                         sorted(file_contents))
