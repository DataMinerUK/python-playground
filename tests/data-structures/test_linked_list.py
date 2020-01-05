import pytest
from src.package.data_structures.linked_list import Node, LinkedList
from unittest import TestCase

class LinkedListTest(TestCase):

    def setup_method(self, method):
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.empty_linked_list = LinkedList()
        self.non_empty_listed_list = LinkedList(1)

    def test_push_to_empty_list(self):
        self.assertEqual(self.empty_linked_list.head, None)
        self.empty_linked_list.push(1)
        self.assertEqual(self.empty_linked_list.head, self.n1)

    def test_push_to_front_of_non_empty_list(self):
        self.non_empty_listed_list.push(2)
        self.assertEqual(self.non_empty_listed_list.head, self.n2)
        self.assertEqual(self.non_empty_listed_list.head.next, self.n1)

    def test_cannot_remove_from_empty_list(self):
        with pytest.raises(IndexError) as index_error:
            self.empty_linked_list.remove()
        assert 'cannot remove from empty list' in str(index_error.value)

    def test_removes_front_of_linked_list_of_one_node(self):
        self.assertEqual(self.non_empty_listed_list.head, self.n1)
        self.non_empty_listed_list.remove()
        self.assertIsNone(self.non_empty_listed_list.head)

    def test_removes_front_of_linked_list_of_two_nodes(self):
        self.non_empty_listed_list.push(2)
        self.assertEqual(self.non_empty_listed_list.head, self.n2)
        self.non_empty_listed_list.remove()
        self.assertEqual(self.non_empty_listed_list.head, self.n1)

    def test_size_of_empty_list_is_zero(self):
        self.assertEqual(self.empty_linked_list.size(), 0)

    def test_size_of_list_with_two_nodes_is_two(self):
        self.non_empty_listed_list.push(2)
        self.assertEqual(self.non_empty_listed_list.size(), 2)

    def test_append_to_back_of_empty_list(self):
        self.empty_linked_list.append(1)
        self.assertEqual(self.empty_linked_list.head, self.n1)

    def test_append_to_back_of_non_empty_list(self):
        self.assertEqual(self.non_empty_listed_list.head, self.n1)
        self.non_empty_listed_list.append(2)
        self.assertEqual(self.non_empty_listed_list.head.next, self.n2)

    def test_cannot_pop_from_empty_list(self):
        with pytest.raises(IndexError) as index_error:
            self.empty_linked_list.pop()
        assert 'cannot pop from empty list' in str(index_error.value)

    def test_pops_back_of_linked_list_of_one_node(self):
        self.assertEqual(self.non_empty_listed_list.head, self.n1)
        self.assertEqual(self.non_empty_listed_list.size(), 1)
        self.non_empty_listed_list.pop()
        self.assertIsNone(self.non_empty_listed_list.head)
        self.assertEqual(self.non_empty_listed_list.size(), 0)

    def test_pops_back_of_linked_list_of_two_nodes(self):
        self.non_empty_listed_list.append(2)
        self.assertEqual(self.non_empty_listed_list.head, self.n1)
        self.assertEqual(self.non_empty_listed_list.head.next, self.n2)
        self.assertEqual(self.non_empty_listed_list.size(), 2)
        self.non_empty_listed_list.pop()
        self.assertEqual(self.non_empty_listed_list.head, self.n1)
        self.assertEqual(self.non_empty_listed_list.size(), 1)
