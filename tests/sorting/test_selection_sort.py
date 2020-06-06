import pytest
import unittest

from src.package.sorting.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        a = [12, 7, 4, 9, 34]
        expected = [4, 7, 9, 12, 34]
        self.assertEqual(selection_sort(a), expected)
