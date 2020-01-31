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
    # node where finder currently is
    current = self.head
    previous = None
   

    while current != None:
      # print('TEST')
      temporary = current
      # print('temp', temporary)
      current = current.set_next(previous)
      # print('current', current)
      # current.get_next() = temporary
      previous = current
      new_node = temporary
      # print('temporary', temporary)

'''
We did this in class
this is where we are going to have to juggle a few variables like in last weeks project

Im going to need to hold the current node
im going to need to hold the previous node
Im going to need to hold the next node

it will all be in a while loop
while the current node is not none
  I think Ill probably need a temperary var to hold for juggling
  ill set temp node to current node
  ill set current node to next node
  ill set next node to the node after current
  the node after current can be set to the temp



'''

'''
Passing 3 tests, 2 errors

# node where finder currently is
    current = self.head
    print('current', current)
    # node after current node
    # new_node = current.get_next
    # new_node = self.get_next
    new_node = None
    # node previous to current node
    previous = None

    while current != None:
      print('TEST')
      temporary = current
      print('temp', temporary)
      current = new_node
      print('current', current)
      new_node = current.get_next
      print('new node', new_node)
      current.get_next = temporary
      print('temporary', temporary)
'''

'''
# node where finder currently is
    current = self.head
    # print('current', current)
    # node after current node
    # new_node = current.get_next
    # new_node = self.get_next
    new_node = current.next_node
    # node previous to current node
    previous = None

    while current != None:
      # print('TEST')
      temporary = current
      # print('temp', temporary)
      current = new_node
      # print('current', current)
      new_node = current.set_next()
      # print('new node', new_node)
      current.get_next = temporary
      # print('temporary', temporary)
'''

'''
Still passing 3 tests, failing differe 2

# node where finder currently is
    current = self.head
   
    # node after current node
    new_node = current.next_node
    current.next_node = None

    while new_node != None:
      # print('TEST')
      temporary = current
      # print('temp', temporary)
      current = new_node
      # print('current', current)
      new_node = current.set_next()
      # print('new node', new_node)
      # current.get_next() = temporary
      current = temporary
      # print('temporary', temporary)
'''

'''
I think Im juggling correctly but there is still returning errors for reversing a single number and an actual list of numbers

I think I have to many variables the new node and previous are interacting wrong

# node where finder currently is
    current = self.head
    previous = None
   
    # node after current node
    # new_node = current.next_node
    # current.next_node = None

    while current != None:
      # print('TEST')
      temporary = current
      # print('temp', temporary)
      current = previous
      # print('current', current)
      new_node = current.set_next(previous)
      # print('new node', new_node)
      # current.get_next() = temporary
      previous = new_node
      new_node = temporary
      # print('temporary', temporary)
'''

'''
Passing 4 tests
for some reason have new_node = temporary (forgot to take it out) passes but when i have current = temporary it fails

# node where finder currently is
    current = self.head
    previous = None
   

    while current != None:
      # print('TEST')
      temporary = current
      # print('temp', temporary)
      current = current.set_next(previous)
      # print('current', current)
      # current.get_next() = temporary
      previous = current
      new_node = temporary
      # print('temporary', temporary)
'''


