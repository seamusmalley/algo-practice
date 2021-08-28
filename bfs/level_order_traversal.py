"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Example 1:
Level Order Traversal:  
    [[1],
     [2,3],
     [4,5,6,7]] 

Example 2:
Level Order Traversal:  
    [[12],
     [7,1],
     [9,10,5]]
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root: Node) -> [[int]]:
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

    return traversal


# Test
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left =  Node(6)
root.right.right = Node(7)

print(level_order_traversal(root))