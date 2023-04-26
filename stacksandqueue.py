# list - time complexity
# search list O(N)
[12, 3, 58, 4, 19].index(4)

# index into a list O(1)
[3,6,19,10][3]

# copy list O(N)
[1,3,9][:]

# removing from end O(1)
[1,2,3].pop()

#removing from specific position O(N)
[12, 3, 58, 4, 19].pop(2)

# stack - last in first out, e.g. can of pringles
stack = []
stack.append(1) # O(1)
stack.append(2) # O(1)
stack.append(3) # O(1)
# implement stack, use .pop() -> popping last element
stack.pop()

# queues - first in first out: carnevale line or waiting list
queues = []
queues.append(1) # O(1)
queues.append(2) # O(1)
queues.append(3) # O(1)

# remove
queues.pop(0) #O(N)

# queues - first in first out: carnevale line or waiting list
queues2 = []
queues2.insert(0, 1) # O(N)
queues2.insert(0, 2) # O(N)
queues2.insert(0, 3) # O(N)

# remove
queues2.pop() #O(1)