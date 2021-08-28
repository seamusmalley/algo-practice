"""
Given a binary tree and a node, find the level order successor of the given node in the tree.
The level order successor is the node that appears right after the given node in the level order traversal.
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def find_lo_successor(root: Node, id: int) -> int:
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

    for i in range(len(traversal)):
        if traversal[i] == id:
            return traversal[i + 1]

    return -1


# Test 1
