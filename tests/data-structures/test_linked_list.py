import pytest
from src.package.data_structures.linked_list import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def test_push_to_empty_list(self):
        n = Node("d")
        l = LinkedList()
        self.assertEqual(l.head, None)
        l.push("d")
        self.assertEqual(l.head, n)

    def test_push_to_front_of_non_empty_list(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.push(1)
        l.push(2)
        self.assertEqual(l.head, n2)
        self.assertEqual(l.head.next, n1)

    def test_cannot_remove_from_empty_list(self):
        l = LinkedList()
        with pytest.raises(IndexError) as index_error:
            l.remove()
        assert 'cannot remove from empty list' in str(index_error.value)

    def test_removes_front_of_linked_list_of_one_node(self):
        l = LinkedList()
        n1 = Node(1)
        l.push(1)
        self.assertEqual(l.head, n1)
        l.remove()
        self.assertIsNone(l.head)

    def test_removes_front_of_linked_list_of_two_nodes(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.push(1)
        l.push(2)
        self.assertEqual(l.head, n2)
        l.remove()
        self.assertEqual(l.head, n1)

    def test_size_of_empty_list_is_zero(self):
        l = LinkedList()
        self.assertEqual(l.size(), 0)

    def test_size_of_list_with_two_nodes_is_two(self):
        l = LinkedList()
        l.push(1)
        l.push(2)
        self.assertEqual(l.size(), 2)

    def test_append_to_back_of_empty_list(self):
        l = LinkedList()
        n1 = Node(1)
        l.append(1)
        self.assertEqual(l.head, n1)

    def test_append_to_back_of_non_empty_list(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.append(1)
        self.assertEqual(l.head, n1)
        l.append(2)
        self.assertEqual(l.head.next, n2)

    def test_cannot_pop_from_empty_list(self):
        l = LinkedList()
        with pytest.raises(IndexError) as index_error:
            l.pop()
        assert 'cannot pop from empty list' in str(index_error.value)

    def test_pops_back_of_linked_list_of_one_node(self):
        l = LinkedList()
        n1 = Node(1)
        l.append(1)
        self.assertEqual(l.head, n1)
        self.assertEqual(l.size(), 1)
        l.pop()
        self.assertIsNone(l.head)
        self.assertEqual(l.size(), 0)

    def test_pops_back_of_linked_list_of_two_nodes(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        l.append(1)
        l.append(2)
        self.assertEqual(l.head, n1)
        self.assertEqual(l.head.next, n2)
        self.assertEqual(l.size(), 2)
        l.pop()
        self.assertEqual(l.head, n1)
        self.assertEqual(l.size(), 1)
