from Node import Node


class DoubleLinked():
    def __init__(self, head = None):
        new_node = Node(head) if (head is not None) else None
        self.head = new_node
        self.tail = new_node

    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head.set_prior(new_node)
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        self.tail.set_next(new_node)
        new_node.set_prior(self.tail)
        # Despite assigning a new value to tail, the orig value pointer still exists
        self.tail = new_node

    def delete_first(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.delete_prior()

    def delete_last(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prior
            self.tail.delete_next()

    def delete_value(self, val):
        previous = None
        current = self.head
        val_present = False

        while current is not None:
            if current.value == val:
                if previous is not None:
                    if current == self.tail:
                        self.tail = previous
                        previous.delete_next()
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

    def clear(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
