"""
solution
	- time O(n)
	- space O(lg(n))
"""

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value


def validate_bst(root: Node) -> bool:
	if not root:
		return True

	if root.left:
		left_is_valid = (root.value > root.left.value) and validate_bst(root.left)
	else:
		left_is_valid = True

	if root.right:
		right_is_valid = (root.value <= root.right.value) and validate_bst(root.right)
	else:
		right_is_valid = True

	return left_is_valid and right_is_valid


# TEST
root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(15)
root.right.left = Node(13)
root.right.left.right = Node(14)
root.right.right = Node(22)

print(validate_bst(root))
