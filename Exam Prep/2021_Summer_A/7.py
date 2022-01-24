from functools import *

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data) + " -> " + str(self.next)

def linked_range(start, end):
    if start != end:
        # return Node(start, linked_range(start+1, end))
        return reduce(lambda next, data: Node(data, next), range(end-2, start-1, -1), Node(end-1))

res = linked_range(2, 5)
print(res)
assert res.data == 2 and res.next.data == 3 and res.next.next.data == 4 and res.next.next.next == None
assert linked_range(2, 2) == None
