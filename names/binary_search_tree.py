from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare root node
        if value < self.value:
            # if lesser go to left child
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                # if something is already there, recurse
                self.left.insert(value)
        else:  # value is > =Node
            # if greater or = go to right child
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                # if something is already there recurse
                self.right.insert(value)

        #  if no childe, on that side, insert
        #  else try again starting from the child on appropriate

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # look at root, if root is it return
        # if no left child, return none
        #  if value is >= node, go right and repeat
        #  if no right child, return none
        if self.value == target:
            return True
        # if value is less than node, go left and repeat
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # RECURSIVE
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()

        # ITERATIVE
        max_value = self.value
        # create a reference to the current node and update it
        # as we traverse the tree
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
        # current.value += 1
        # print(self.value)

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
        # if node is None:
        print(node.value)
        if self.left:
            self.left.in_order_print(node)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Need a queue
        queue = Queue()
        # add to queue
        queue.enqueue(node)
        # while the queue is not 0
        while queue.len() > 0:
            # remove the node from the head
            node = queue.dequeue()
            print(node.value)
            # look left
            if node.left is not None:
                # add the node
                queue.enqueue(node.left)
            if node.right is not None:
                # add the node
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # Iterative:
        # make a stack
        stack = Stack()
        # add root to stack
        # print('stack'. stack)
        # pop num and save in temp
        stack.push(node)
        while stack.len() > 0:
            # Do the thing!!
            node = stack.pop()
        # if temp.left add to stack
            print(node.value)
            if node.left is not None:
                stack.push(node.left)
        # if temp.right add to stack
            if node.right is not None:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


'''
from geeks for geeks
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
There must be no duplicate nodes.
'''

'''
  def insert(self, value):
    # call the BinarySearchTree and pass in the value. set it to node.
    
    # check if the insert value is less than the current value, we go left
      # and check if there is no left node, then left node becomes the leaf node
      # otherwise we recursively call insert() again on the left leaf node
    # else that means the inserted value >= current value, we go right 
      # check if right node is none, then right node becomes the leaf node
      # otherwise we recursively call insert() again on the left leaf node
'''


'''
# base case
        if value == None or value == key:
            return None
'''

'''
while queue.len() != 0:
            current = queue.dequeue()

            if current.left:
                queue.enqueue(current.left)
            
            if current.right:
                queue.enqueue(current.right)
'''

'''
while self.stack != None:
            current = self.stack.pop()
        # Do the thing!!
        # if temp.left add to stack
            if node.left:
                self.stack.push(node.left())
        # if temp.right add to stack
            if node.right:
                self.stack.push(node.right())
'''
