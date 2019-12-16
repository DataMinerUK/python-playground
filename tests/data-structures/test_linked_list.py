from src.package.data_structures.linked_list import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def test_append_to_empty_list(self):
        n = Node("d")
        l = LinkedList()
        self.assertEqual(l.head, None)
        l.append("d")
        self.assertEqual(l.head, n)

    def test_append_to_non_empty_list(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.append(1)
        l.append(2)
        self.assertEqual(l.head, n2)
        self.assertEqual(l.head.next, n1)
