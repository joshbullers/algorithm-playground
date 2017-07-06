from Node import Node


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
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete_last(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next

            # by removing references, collection will remove from memory
            current.next = None
            self.tail = current

    def delete_value(self, val):
        previous = None
        current = self.head
        val_present = False

        while current is not None:
            if current.value == val:
                if previous is not None:
                    if current == self.tail:
                        self.tail = previous
                        previous.next = None
                    else:
                        previous.next = current.next
                else:
                    self.head = current.next

                val_present = True
            else:
                previous = current

            current = current.next

        return val_present

    def contains(self, val):
        current = self.head
        while current is not None:
            if current.value == val:
                return True

            current = current.next

        return False

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
