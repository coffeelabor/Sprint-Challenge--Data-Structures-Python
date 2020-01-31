from doubly_linked_list import DoublyLinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity        #limit
    self.current = 0                # position/size
    self.order = DoublyLinkedList() #order
    self.storage = [None]*capacity  #storage

  def append(self, item):
    # I need to make sure the current size/position is less than capacity
    if self.current < self.capacity:
      # the item that being passed in needs to be added to storage
      # item = self.storage[self.current]
      self.storage[self.current] = item
      self.current += 1
      
    
    # I need to check of the storage is at capacity
    if self.current == self.capacity:
      # if it is I need to set the current position to the oldest item
      self.current = 0
    
    # I need to set the storages to the current size
    self.current += 1
    # self.storage.order.add_to_head(item)
    self.storage.append(item)
    print('storage', self.storage)

  def get(self):
    # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        for index in self.storage:
          if index is not None:
            list_buffer_contents.append(index)

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
