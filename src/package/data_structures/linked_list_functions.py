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
