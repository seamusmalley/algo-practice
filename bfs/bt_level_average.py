"""
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def level_average(root: Node) -> [float]:
    result = []

    if not root:
        return result

    queue = [root]

    while len(queue) > 0:
        level_sum, num_nodes = 0.0, 0

        for _ in range(len(queue)):
            node = queue.pop(0)
            level_sum += node.value
            num_nodes += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / num_nodes)

    return result


# Test 1
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
print(level_average(root))

# Test 2
root = Node(12)
root.left = Node(7)
root.left.left = Node(9)
root.left.right = Node(2)
root.right = Node(1)
root.right.left = Node(10)
root.right.right = Node(5)
print(level_average(root))