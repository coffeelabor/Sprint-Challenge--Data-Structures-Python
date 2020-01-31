from doubly_linked_list import DoublyLinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    pass

  def get(self):
    # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents


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
