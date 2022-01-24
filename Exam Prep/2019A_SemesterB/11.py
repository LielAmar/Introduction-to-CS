class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

    def __str__(self):
        return "[" + str(self.data) + "], " + str(self.next)

class LinkedList:
    def __init__(self, head):
        self.head = head
    
    def sort(self):
        self.head = self.sort_helper(self.head)

    def sort_helper(self, curr):
        if curr == None or curr.next == None:
            return curr
               
        result = self.sort_helper(curr.next)
        
        if not result:
            return curr

        return self.insert_at_right_spot(curr, result)


    def insert_at_right_spot(self, curr, result):
        if curr.data < result.data:
            curr.next = result
            return curr
        
        result_head = result

        while result.next and result.next.data < curr.data:
            result = result.next
        
        old_next = result.next
        result.next = curr
        curr.next = old_next

        return result_head
    
    def __str__(self):
        return str(self.head)

if __name__ == "__main__":
    lst = LinkedList(Node(9))
    lst.head.next = Node(-3)
    lst.head.next.next = Node(4)
    lst.head.next.next.next = Node(1)
    lst.head.next.next.next.next = Node(8)

    lst.sort()
    print(lst)