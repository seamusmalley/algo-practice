"""
problem
	- input: binary tree
	- output: [int] of sum of each branch, left to right
"""


class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def end_of_branch(node: Node) -> bool:
	if node.left or node.right:
		return False
	return True


def branch_sums(node: Node, sum: int = 0) -> [int]:
	if not node:
		return []

	sum += node.value

	if end_of_branch(node):
		return [sum]

	l_branch = branch_sums(node.left, sum)
	r_branch = branch_sums(node.right, sum)

	return l_branch + r_branch


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.left.right.left = Node(10)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

print(branch_sums(root))
