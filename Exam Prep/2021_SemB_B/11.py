class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def kth_smallest(root, k):
    if not root:
        return None

    if not root.left and not root.right:
        return root.value
    
    left_children = number_children(root.left)
    
    # If we have exactly k-1 left children it means  that root is the number
    # we're looking for
    if left_children == k-1:
        return root.value
    
    # If we have at least k smaller numbers than root
    elif left_children >= k:
        return kth_smallest(root.left, k)
    
    # If we have less than k smaller numbers than root, the number we're looking
    # for is in the right hand side of the tree
    else:
        return kth_smallest(root.right, k-left_children)


def number_children(root):
    if not root: return 0
    if not (root.left or root.right): return 1
    
    return 1 + number_children(root.left) + number_children(root.right)

if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.right = TreeNode(14)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(27)
    root.right.right.right = TreeNode(300)