class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __eq__(self, other):
        return self.data == other.data


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
