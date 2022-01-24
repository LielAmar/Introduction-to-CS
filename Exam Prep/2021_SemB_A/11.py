class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __eq__(self, other):
        if other is None:
            return False
        
        return self.data == other.data and self.next == other.next

    def __str__(self):
        return str(self.data) + " -> " + str(self.next)

def linked_filter(f, lnk):
    head, linker, pointer = None, None, lnk

    while pointer is not None:
        if f(pointer.data):
            if head == None:
                head = pointer
                linker = head
            else:
                linker.next = pointer
                linker = linker.next
                
        pointer = pointer.next

    return head

if __name__ == "__main__":
    res = linked_filter(lambda x: (x + 1) % 2, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    print(res)
    assert res == Node(2, Node(4, Node(6)))

    res = linked_filter(lambda x: (x + 1) % 2, None)
    print(res)
    assert res == None
    