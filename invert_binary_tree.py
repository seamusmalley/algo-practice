"""
problem
	- input: binary tree
	- output: inverted input tree
	-

solution
	invert(tree):
		swap children
		invert left
		invert right
"""

"""
				1
            /   	\
		   3         2
        /   \      /   \
      7      6    5     4
                       /  \ 
                      9    8
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def swap_children(root: Node):
    root.left, root.right = root.right, root.left


def invert_binary_tree(root: Node) -> Node:
    if root:
        swap_children(root)
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)

    return root


def print_bt(root: Node):
    if not root:
        return

    queue = [root]
    result = []

    while queue:
        result.append(queue[0].value)
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(result)


""" TEST """
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
print_bt(root)
print()

root_invert = invert_binary_tree(root)
print_bt(root_invert)
