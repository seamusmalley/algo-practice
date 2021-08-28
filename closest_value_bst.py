import sys

"""
problem
	- input: BST, target int
	- output: closest value to target in BST
	- only one closest value

solution
	- binary search, check to make sure current val isnt better
	- time O(n)
	- space O(1)
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def closest_value_bst(node: Node, target: int) -> [int]:
    # error on empty tree
    if not node:
        return sys.maxsize

    x = node.value

    if x == target:
        return x

    x_dif = abs(x - target)

    if x < target:
        y = closest_value_bst(node.right, target)
    else:
        y = closest_value_bst(node.left, target)

    y_dif = abs(y - target)

    return x if x_dif < y_dif else y


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(15)
root.right.left = Node(13)
root.right.left.right = Node(14)
root.right.right = Node(22)

print(closest_value_bst(root, 12))
