class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __repr__(self):
        return 'Node(' + repr(self.data) + ( ',' + repr(self.next)) if self.next else '' + ')'

    def __str__(self):
        st = "<"
        while self.next is not None:
            st += str(self.data) + " "
            self = self.next
        return st + str(self.data) + ">"

def f10(lnk):
    if lnk is not None:
        yield from f10(lnk.next)
        yield lnk.data

print(next(f10(Node(1, Node(3)))))
print(list(f10(Node(1, Node(3, Node(2))))))

print(Node(1, Node(3, Node(2))))
print(repr(Node(1, Node(3, Node(2)))))

# 3
# [2, 3, 1]