class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

def connect_levels(root: Node) -> None:
    if not root:
        return

    queue = [root]

    while len(queue) > 0:
        level = []

        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        for i in range(len(level)-1):
            level[i].next = level[i+1]


def print_levels(root: Node) -> None:
    print('Tree Levels')
    i = 0
    node = root
    while node:
        root = node
        level = [node.value]
        while node.next:
            level.append(node.next.value)
            node = node.next
        print(i, ':', level)
        node = root.left
        i += 1

# Test 1
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
connect_levels(root)
print_levels(root)

# Test 2
root = Node(12)
root.left = Node(7)
root.left.left = Node(9)
root.right = Node(1)
root.right.left = Node(10)
root.right.right = Node(5)
connect_levels(root)
print_levels(root)