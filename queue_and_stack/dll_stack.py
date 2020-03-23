import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.items = []
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.items.insert(0, value)

    def pop(self):
        if self.items == []:
            return None
        else:
            return self.items.pop(0)

    def len(self):
        return len(self.items)
