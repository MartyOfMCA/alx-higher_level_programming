#!/usr/bin/python3
""" This module defines a test class for the Base class """
import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted('[{"x": 2, "width": 10, "id": 1, "height": 7'
                                ', "y": 8}]'), sorted(json_dictionary))
