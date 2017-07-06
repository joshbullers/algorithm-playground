class Node():
    def __init__(self, value, nextVal = None):
        self.value = value
        self.next = nextVal

    def set_next(self, nextConnect):
        self.next = nextConnect

    def delete_next(self):
        self.next = None
