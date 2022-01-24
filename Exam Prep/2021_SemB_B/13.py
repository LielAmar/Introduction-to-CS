class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return repr(self.data) + "->" + repr(self.next)

def split_sorted(head):
    if not head: return []
    
    result = [head]
    
    while head.next and head.next.data > head.data: head = head.next
        
    next, head.next = head.next, None
    return result + split_sorted(next)
        
    
if __name__ == "__main__":
    my_node = Node(1, Node(2, Node(3, Node(2, Node(1,Node(10))))))
    assert str(split_sorted(my_node)) == "[1->2->3->None, 2->None, 1->10->None]"
    
    my_node2 = Node(1, Node(2, Node(3, Node(4))))
    assert str(split_sorted(my_node2)) == "[1->2->3->4->None]"
    
    my_node3 = Node(10, Node(9, Node(8, Node(3, Node(1)))))
    assert str(split_sorted(my_node3)) == "[10->None, 9->None, 8->None, 3->None, 1->None]"