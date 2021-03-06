import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is lower then node
        if value < self.value:
            # if left node is empty insert value
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)

        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass
        # if node.left:
        #     self.left.in_order_print(node.left)
        #
        # return print(node.value)
        #
        # if node.right:
        #     self.right.in_order_print(node.right)
        #
        # return node.value


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)

        while queue.len() > 0:
            n = queue.dequeue()
            print(n.value)

            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)

        while stack.len() > 0:
            n = stack.pop()
            print(n.value)

            if n.left:
                stack.push(n.left)
            if n.right:
                stack.push(n.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
