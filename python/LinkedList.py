from Node import Node
from ctypes import addressof


class LinkedList():
    def __init__(self, head = None):
        new_node = Node(head) if (head is not None) else None
        self.head = new_node
        self.tail = new_node

    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        self.tail.set_next(new_node)
        # Despite assigning a new value to tail, the orig value pointer still exists
        self.tail = new_node

    def delete_first(self):


    def delete_last(self):
        if self.head == self.tail:
            del self.head
            del self.tail
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
