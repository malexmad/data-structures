from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit                # setting default or given limit
        self.items = DoublyLinkedList()
        self.storage = {}                 # dictionary


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:                           # looping thru dict for key
            self.items.move_to_front(self.storage[key])   # if key is in dict move that node to the front
            return self.storage[key].value[1]             # return the value

        else:
            return None                                   # return none if key is not in dict

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key is in storage, move that node to the front of the list no need to add
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            return self.items.move_to_front(node)

        # if size is smaller then limit add key, value as a node and in cache
        if len(self.items) < self.limit:
            self.items.add_to_head((key, value))
            self.storage[key] = self.items.head

        # If length equal to limit remove the tail and the key, value from the dict and add new node to the head
        elif len(self.items) == self.limit:
            del self.storage[self.items.remove_from_tail()[0]]
            self.items.remove_from_tail()
            self.items.add_to_head((key, value))
            self.storage[key] = self.items.head


