class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    
    # I need a current value to for the node to tell where it is 
    current = self
    print(f'current {current}')
    # I need to set a new value so it can go to the node next of it
    new_value = current.get_next()
    set_new = set_next()
    # I should set the current.next node to None to initialize it
    # current.set_next() = None
    set_new = None
    # I should start a while loop with new != None
    while new_value != None:
        # I need a new var to act as a temp value so I can shuffle the items
      previous = current
        # I should set the current value to the new value so I can itterate through the list
      current = new_value
        # I should set the new value to the current.next value to increase it
      new_value = current.get_next()
        # I should set the current.next value to the prev value
      current.set_next = previous
    # I should return current
    return current













'''
current = self.head
new = current.get_next()
  # current.set_next() = None
  while new != None:
      prev = current
      current = new
      new = current.next_node
      current.next = prev
  # print(current)
  return current

'''
