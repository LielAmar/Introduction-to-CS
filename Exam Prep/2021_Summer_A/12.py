class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def closest_value(root, target):
    if not root: return

    if not (root.left or root.right):
        return root.value
    
    if root.value == target:
        return root.value

    closest = root.value

    if root.value > target:
        result = closest_value(root.left, target)
    else:
        result = closest_value(root.right, target)

    if result:
        if abs(result - target) < abs(closest - target):
            closest = result

    return closest

if __name__ == "__main__":
    root = TreeNode(9)
    root.left = TreeNode(5)
    root.right = TreeNode(26)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(30)
    root.right.right.right = TreeNode(100)

    assert closest_value(root, 1) == 2
    assert closest_value(root, 2) == 2
    assert closest_value(root, 8) == 7 or closest_value(root, 8) == 9
    assert closest_value(root, 29) == 30
    assert closest_value(root, 80) == 100
    assert closest_value(root, 105) == 100