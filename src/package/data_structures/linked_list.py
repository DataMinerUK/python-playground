class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def remove(self):
        if not self.head:
            raise IndexError('cannot remove from empty list')
        self.head = self.head.next

    # def size
    # def append
    # def pop
