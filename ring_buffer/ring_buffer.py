class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # limit
        self.current = 0  # size
        self.storage = [None]*capacity  # storage

    

    #I want to use the lru_cache for this
    def append(self, item):
        # I need to add the items from head -> tail and keep track of when they were added
        # I need to loop through the ringbuffer from head -> tail
        # I need to check if the size of the list is at the limit passed in
          # If true,than I need to replace the oldest values with new ones being added in order 
        pass
        
    def get(self):
        if self.storage:
          node = self.storage
          return node.storage
        else:
          return None


# buffer = RingBuffer(5)

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')


'''
if key in self.storage:
          node = self.storage[key]
          node.item = (key, value)
'''
'''
# def append(self, key, item):
        # self.current += 1
        # self.storage.append(item)
        # print(self.storage)
'''

'''
Tried this first for the append

if item in self.storage:
          node = self.storage[item]
          node.item = item
        print(self.storage)
        if self.current == self.capacity:
          del self.storage[self.storage[0]]
        self.append(item)
        self.storage[item] = self.storage[-1]

I tried adding this to get the above to work right
# def add_to_tail(self, value):
    #     new_node = RingBuffer(capacity, None, None)
    #     # self.length += 1
    #     if not self.head and not self.tail:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         new_node.prev = self.tail
    #         self.tail.next = new_node
    #         self.tail = new_node
'''

