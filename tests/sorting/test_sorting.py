import pytest
import unittest

from src.package.sorting.sorting import *

class TestSorting(unittest.TestCase):

    def test_selection_sort(self):
        a = [12, 7, 4, 9, 34]
        expected = [4, 7, 9, 12, 34]
        self.assertEqual(selection_sort(a), expected)

    def test_bubble_sort(self):
        a = [12, 7, 4, 9, 34]
        expected = [4, 7, 9, 12, 34]
        self.assertEqual(bubble_sort(a), expected)

    def test_insertion_sort(self):
        a = [12, 7, 4, 9, 34]
        expected = [4, 7, 9, 12, 34]
        self.assertEqual(bubble_sort(a), expected)
