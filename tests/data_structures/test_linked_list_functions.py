import pytest
import unittest
from src.package.data_structures.linked_list import Node, LinkedList
from src.package.data_structures.linked_list_functions import *

class LinkedListFunctionsTest(unittest.TestCase):

    def test_reverse_empty_list(self):
        l = LinkedList()
        self.assertIsNone(reverse(l).head)

    def test_reverse_linked_list_1_2_equals_2_1(self):
        l = LinkedList(1)
        l.append(2)
        reversed = reverse(l)
        self.assertEqual(reversed.head, Node(2))
        self.assertEqual(reversed.head.next, Node(1))

    def test_get_nth_node_out_of_range(self):
        l = LinkedList(1)
        with pytest.raises(IndexError) as index_error:
            get_nth(1, l)
        assert 'Index out of range' in str(index_error.value)

    def test_get_nth_node(self):
        l = LinkedList(1)
        l.append(2)
        self.assertEqual(get_nth(0, l), Node(1))
        self.assertEqual(get_nth(1, l), Node(2))
