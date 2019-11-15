import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

'''
I need to go through each list and compare to it to each other so I can look for duplicates
A binary search tree would cut the search time in half cause it would only to go through half of the lists each time
right now the runtime is (n^2) since it is a loop within a loop
a binary search tree has (log n) search time since it is halving every time
I guess I could make the first item in the list the root node, and compare everything against that to see if 


'''