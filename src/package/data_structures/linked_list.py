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

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            tail = self.__get_tail()
            tail.next = node

    def __get_tail(self):
        tail = self.head
        if tail:
            while tail.next:
                tail = tail.next
        return tail
    # def pop
