"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def reverse_order_traversal(root: Node) -> [[int]]:
    traversal = []

    if not root:
        return traversal

    queue = [root]

    while len(queue) > 0:
        level = []

        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        traversal.append(level)

    return traversal[::-1]


# Take 2
def reverse_order_traversal(root: Node) -> [[int]]:
    traversal = []

    if not root:
        return traversal

    queue = [root]

    while len(queue) > 0:
        level = []
        
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        traversal = [level] + traversal

    return traversal


# Test
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left =  Node(6)
root.right.right = Node(7)

print(reverse_order_traversal(root))