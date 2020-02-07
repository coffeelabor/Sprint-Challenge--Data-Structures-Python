from doubly_linked_list import DoublyLinkedList, ListNode


class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity        # limit
    self.current = None                # position/size
    # self.order = dict()             # storage
    self.storage = DoublyLinkedList()

  def append(self, item):
    # Make sur the length from the dll is less than the limit of the ring
    if self.storage.length < self.capacity:
      # Add the Item to the head of the list
      self.storage.add_to_head(item)
      # get the finder to the tail of the list
      self.current = self.storage.tail

    #Check if the finder is at the tail already
    elif self.current == self.storage.tail:
      # the tail item is the oldest item at this point so removed
      self.storage.remove_from_tail()
      # replace that old item with the new one
      self.storage.add_to_tail(item)
      # move the finder to the previous node witch is now the oldest item
      self.current = self.current.prev

    # Check If the finder is at the head
    elif self.current == self.storage.head:
      # the head is the oldest item so it needs to be removed
      self.storage.remove_from_head()
      # replace the old item with the new one
      self.storage.add_to_head(item)
      # since there is no prev on head, set finder to tail
      self.current = self.storage.tail

    # the finder is between the head and tail
    else:
      # The item gets inserted after where the finder is
      self.current.insert_after(item)
      # since the list is +1 past capacity and the wrong item is in the list, delete
      self.current.delete()
      # keep moving the finder toward the head
      self.current = self.current.prev

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # TODO: Your code here
    # Set a temp variable to one of the ends of the array
    temporary = self.storage.tail
    # loop until it reaches the end
    while temporary != None:
      # Append each value to the buffer
      list_buffer_contents.append(temporary.value)
      # move through the array
      temporary = temporary.prev

    print('list buffer', list_buffer_contents)
    return list_buffer_contents
          


# ----------------Stretch Goal-------------------
class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


'''
A ring buffer is a non-growable buffer with a fixed size. 

When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. 

Implement this behavior in the RingBuffer class. 

RingBuffer has two methods, `append` and `get`. 

    The `append` method adds elements to the buffer. 
    
    The `get` method returns all of the elements in the buffer in a list in their given order. 

    It should not return any `None` values in the list even if they are present in the ring buffer.
'''

'''
Since this is removing old Items it will be like the lru cache

for the get I can just do for index in self.storage and fileter for not None
  if not none
    append to the array

I dont think I need order since its a ring

the current can be used as a posistion but it cannot go over the size
  its test for a ring array of capicty = 5 so != be position of 6
'''

'''
if item in self.storage:
      node = self.storage[item]
      node.item = (item)
      self.order.move_to_end(node)
      return
'''

'''
# I need to make sure the current size/position is less than capacity
    if self.current < self.capacity:
      # the item that being passed in needs to be added to storage
      item = self.storage[self.current]
      
    
    # I need to check of the storage is at capacity
    if self.capacity == self.storage:
      # if it is I need to set the current position to the oldest item
      self.current = 0
    
    # I need to set the storages to the current size
    self.current += 1
    self.storage.order.add_to_head(item)
    print('storage', self.storage)
'''
'''
def append(self, item):
    # I need to make sure the current size/position is less than capacity
    if self.current < self.capacity:
      # the item that being passed in needs to be added to storage
      # item = self.storage[self.current]
      # set the index of the storage to the current position and set it to item
      self.storage[self.current] = item
      # increase the size by 1
      self.current += 1
      
    
    # I need to check of the storage is at capacity
    if self.current == self.capacity:
      # if current size == capacity, set the current position to the oldest item
      self.current = 0
    
    # I need to set the storages to the current size
    self.current += 1
    # self.storage.order.add_to_head(item)
    # add the item to storage
    self.storage(self.order.add_to_head(item))
    # self.storage.append(item)
    print('storage', self.storage)

'''
'''
self.capacity = capacity        #limit
    self.current = 0                # position/size
    self.order = DoublyLinkedList() #order
    self.storage = [None]*capacity  #storage
'''

'''
# I need to make sure the current size/position is less than capacity
    if self.current < self.capacity:
      # set the index of the storage to the current position and set it to item
      self.storage[self.current] = item
      # increase the size by 1
      self.current += 1
      
    
    # I need to check of the storage is at capacity
    if self.current == self.capacity:
      # if current size == capacity, set the current position to the oldest item
      self.current = 0
    
    # I need to set the storages to the current size
    self.current += 1
    # add the item to storage
    self.storage(self.order.add_to_head(item))
    print('storage', self.storage)
'''

'''
if item in self.storage:
      node = self.storage[item]
      self.storage.move_to_end(node)
    if self.current == self.capacity:
      del self.storage[self.storage.head.item[0]]
      self.storage.remove_from_head()
      self.current -=1
    
    self.storage.add_to_tail(item)
    self.storage[item] = self.storage.tail
    self.current +=1
'''
'''
if item in self.storage:
      node = self.storage[item]
      self.storage.move_to_end(node)
    if self.current == self.capacity:
      del self.storage[self.storage.head.item[0]]
      self.storage.remove_from_head()
      self.current -=1
    
    self.storage.add_to_tail(item)
    self.storage[item] = self.storage.tail
    self.current +=1
'''
'''
count = 0
    while count < self.storage.length:
      tail = self.storage.tail
      list_buffer_contents.append(tail.value)
      self.storage.move_to_front(tail)
      count += 1

    print('list buffer', list_buffer_contents)
    return list_buffer_contents
'''



'''
# Prints and lists the items in the array

def __init__(self, capacity):
    self.capacity = capacity        # limit
    self.current = 0                # position/size
    self.order = DoublyLinkedList()  # order
    self.storage = [None]*capacity  # storage

  def append(self, item):

# I need to make sure the current size/position is less than capacity
    if self.current < self.capacity:
      # the item that being passed in needs to be added to storage
      # item = self.storage[self.current]
      # set the index of the storage to the current position and set it to item
      self.storage[self.current] = item
      # increase the size by 1
      self.current += 1

    # I need to check of the storage is at capacity
    if self.current == self.capacity:
      # if current size == capacity, set the current position to the oldest item
      self.current = 0

    # I need to set the storages to the current size
    self.current += 1
    # self.storage.order.add_to_head(item)
    # add the item to storage
    # self.storage(self.order.add_to_head(item))
    self.storage.append(item)
    # self.storage.append(item)
    print('storage', self.storage)

'''
'''
I might be on the right track here, but I want to work on a different approach
COME BACK TO THIS 

from doubly_linked_list import DoublyLinkedList, ListNode

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity        # limit
    self.current = 0                # position/size
    self.storage = DoublyLinkedList()  # storage

  def append(self, item):
    # The length of the ringBuffer should not exceed the capacity 
    if len(self.storage) < self.capacity:
      # Use the dll method of add to head to insert the item to the front
      self.storage.add_to_head(item)
      # increase the size by 1
      self.current =+ 1

    # I need to check of the storage is at capacity
    if self.current == self.capacity:
      # if current size == capacity, remove the tail which is the oldest item
      self.storage.remove_from_tail()
      self.current -= 1

    print('storage', self.storage)


  def get(self):
    # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        for index in self.storage.value:
          if index is not None:
            list_buffer_contents.append(index)
        print('list buffer', list_buffer_contents)
        return list_buffer_contents


'''

'''
def append(self, item):
    # Make sur the length from the dll is less than the limit of the ring
    if self.storage.length < self.capacity:
      # Add the Item to the head of the list
      self.storage.add_to_head(item)
      # get the finder to the tail of the list
      self.current = self.storage.tail
    
    #Check if the finder is at the tail already 
    elif self.current == self.storage.tail:
      # the tail item is the oldest item at this point so removed
      self.storage.remove_from_tail()
      # replace that old item with the new one
      self.storage.add_to_tail(item)
      # move the finder to the previous node witch is now the oldest item
      self.current = self.current.head
    
    # Check If the finder is at the head 
    else self.current == self.storage.head:
      # the head is the oldest item so it needs to be removed
      self.storage.remove_from_head()
      # replace the old item with the new one
      self.storage.add_to_head(item)
      # since there is no prev on head, set finder to tail
      self.current = self.storage.tail
    
    # If the finder is in the middle somewhere 
    while self.current != self.storage.head and self.current != self.storage.tail:
      #  Work throught the list and add in items
       self.current.insert_before(item)
      #  Move through the middle
       self.current = self.current.next

'''
'''
# If the finder is in the middle somewhere
    while self.current != self.storage.head and self.current != self.storage.tail:
      #  Work throught the list and add in items
       self.current.insert_after(item)
      #  Move through the middle
       self.current = self.current.prev
'''

'''
Didnt really work that well

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity        # limit
    self.current = 0                # position/size
    # self.order = dict()             # storage
    self.storage = DoublyLinkedList()            
  def append(self, item):
    if item in self.order:
      node = self.order[item]
      node.value = (item)
      self.storage.move_to_end(node)
      return

    if self.current == self.capacity:
        del self.order[self.storage.head.value[0]]
        self.storage.remove_from_head()
        self.current -=1


    self.storage.add_to_tail((item))
    self.order[item] = self.storage.tail
    self.current += 1


  def get(self):
    # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        for index in self.current:
          if index is not None:
            list_buffer_contents.append(key)
        return list_buffer_contents
'''

'''
This should add to each of the ends then fill in the middle, hitting errors

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity        # limit
    self.current = None                # position/size
    # self.order = dict()             # storage
    self.storage = DoublyLinkedList()

  def append(self, item):
    # Make sur the length from the dll is less than the limit of the ring
    if self.storage.length < self.capacity:
      # Add the Item to the tail of the list
      self.storage.add_to_tail(item)
      # get the finder to the head of the list
      self.current = self.storage.head

    #Check if the finder is at the tail already
    elif self.current == self.storage.tail:
      # the tail item is the oldest item at this point so removed
      self.storage.remove_from_tail()
      # replace that old item with the new one
      self.storage.add_to_tail(item)
      # since there is no prev on head, set finder to head
      self.current = self.storage.head

    # Check If the finder is at the head
    elif self.current == self.storage.head:
      # the head is the oldest item so it needs to be removed
      self.storage.remove_from_head()
      # replace the old item with the new one
      self.storage.add_to_head(item)
      # move the finder to the next node witch is now the oldest item
      self.current = self.current.next

    # the finder is between the head and tail
    else:
      # The item gets inserted before where the finder is
      self.current.insert_before(item)
      # since the list is +1 past capacity and the wrong item is in the list, delete
      self.current.delete()
      # keep moving the finder toward the tail
      self.current = self.current.next

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # TODO: Your code here
    # Set a temp variable to one of the ends of the array
    temporary = self.storage.head
    # loop until it reaches the end
    while temporary != None:
      # Append each value to the buffer
      list_buffer_contents.append(temporary.value)
      # move through the array
      temporary = temporary.next

    print('list buffer', list_buffer_contents)
    return list_buffer_contents
'''


'''
Doint the first three tests right

def append(self, item):
    # Make sur the length from the dll is less than the limit of the ring
    if self.storage.length < self.capacity:
      # Add the Item to the tail of the list
      self.storage.add_to_tail(item)
      # get the finder to the head of the list
      self.current = self.storage.head

    #Check if the finder is at the tail already
    elif self.current == self.storage.tail:
      # the tail item is the oldest item at this point so removed
      self.storage.remove_from_tail()
      # replace that old item with the new one
      self.storage.add_to_tail(item)
      # move the finder to the previous node witch is now the oldest item
      self.current = self.current.prev

    # Check If the finder is at the head
    elif self.current == self.storage.head:
      # the head is the oldest item so it needs to be removed
      self.storage.remove_from_head()
      # replace the old item with the new one
      self.storage.add_to_head(item)
      # since there is no prev on head, set finder to tail
      self.current = self.storage.tail

    # the finder is between the head and tail
    else:
      # The item gets inserted after where the finder is
      self.current.insert_before(item)
      # since the list is +1 past capacity and the wrong item is in the list, delete
      self.current.delete()
      # keep moving the finder toward the head
      self.current = self.current.next

  def get(self):
    # Note:  This is the only [] allowed
    list_buffer_contents = []

    # TODO: Your code here
    # Set a temp variable to one of the ends of the array
    temporary = self.storage.head
    # loop until it reaches the end
    while temporary != None:
      # Append each value to the buffer
      list_buffer_contents.append(temporary.value)
      # move through the array
      temporary = temporary.next

    print('list buffer', list_buffer_contents)
    return list_buffer_contents
'''

