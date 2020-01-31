import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

binary_search = BinarySearchTree(None)

# Insert names into list
for name in names_1:
    binary_search.insert(name)

# Compare names in list
for name_check in names_2:
    # Going through each name from names_1 and comparing to names_2
    if binary_search.contains(name_check):
        # If names_1 contains names_2 then the name is appended to duplicates
        duplicates.append(name_check)
    
        # return

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

'''
# Runtime is O(n^2)
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

'''
Im going to need to insert all the names into the search tree
    I think I can just start with one of the lists
    I will use insert
for the second list I can just compare everyting against the first list
    the tree will be loaded with the names of one list already
    I can use contains here
'''