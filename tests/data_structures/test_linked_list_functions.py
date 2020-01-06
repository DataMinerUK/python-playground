import pytest
import unittest
from src.package.data_structures.linked_list import Node, LinkedList
from src.package.data_structures.linked_list_functions import reverse

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
