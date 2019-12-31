from src.package.data_structures.linked_list import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def test_push_to_empty_list(self):
        n = Node("d")
        l = LinkedList()
        self.assertEqual(l.head, None)
        l.push("d")
        self.assertEqual(l.head, n)

    def test_push_to_non_empty_list(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.push(1)
        l.push(2)
        self.assertEqual(l.head, n2)
        self.assertEqual(l.head.next, n1)
