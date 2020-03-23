import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.items = []
#
#     def push(self, value):
#         self.items.insert(0, value)
#
#     def pop(self):
#         if self.items == []:
#             return None
#         else:
#             return self.items.pop(0)
#
#     def len(self):
#         return len(self.items)
