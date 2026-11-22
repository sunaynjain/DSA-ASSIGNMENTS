# BST - Level Wise Display, Height and Leaf Nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# Level-wise display
def level_order(root):
    if root is None:
        print("Tree is empty.")
        return

    queue = [root]

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        print()

# Height of tree (number of levels)
def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)

# Print leaf nodes
def print_leaves(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return

    print_leaves(root.left)
    print_leaves(root.right)

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input("Enter value: "))
    root = insert(root, value)

print("\nOriginal BST Level Wise:")
level_order(root)

new_value = int(input("\nEnter new value to insert: "))
root = insert(root, new_value)

print("\nUpdated BST Level Wise:")
level_order(root)

print("\nHeight of BST:", height(root))

print("Leaf Nodes:")
print_leaves(root)
print()
