"""
Given a binary tree, populate an array to represent its zigzag level order traversal. 
You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels.
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def zigzag_traversal(root: Node) -> [[int]]:
    traversal = []
    zig = True

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

        if zig == True:
            traversal.append(level)
        else:
            traversal.append(level[::-1])
        zig = not zig

    """ other way of flipping
    for i in range(len(traversal)):
        if i % 2 != 0:
            traversal[i] = traversal[i][::-1]
    """

    return traversal

# Test 1
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left =  Node(6)
root.right.right = Node(7)
print(zigzag_traversal(root))


# Test 2 
root = Node(12)
root.left = Node(7)
root.left.left = Node(9)
root.right = Node(1)
root.right.left = Node(10)
root.right.left.left = Node(20)
root.right.left.right = Node(17)
root.right.right = Node(5)
print(zigzag_traversal(root))