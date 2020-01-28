from src.package.data_structures.linked_list import LinkedList

def reverse(linked_list):
    if not linked_list.head:
        return linked_list
    else:
        reversed = LinkedList(linked_list.pop().data)
        current = reversed.head
        while linked_list.head:
            current.next = linked_list.pop()
            current = current.next
        return reversed

def get_nth(n, linked_list):
    if linked_list.size() - 1 < n :
        raise IndexError('Index out of range')
    current = linked_list.head
    for i in range(n):
        current = current.next
    return current

def get_middle(linked_list):
    length = linked_list.size()
    if length < 1:
        raise IndexError('Index out of range')
    middle = length/2
    current = linked_list.head
    for i in range(int(middle)):
        current = current.next
    return current
