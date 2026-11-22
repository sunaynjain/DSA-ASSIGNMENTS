# Library Catalog Navigation using Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create library category tree
root = Node("Library")

root.left = Node("Science")
root.right = Node("Arts")

root.left.left = Node("Physics")
root.left.right = Node("Chemistry")

root.right.left = Node("History")
root.right.right = Node("Literature")

root.left.left.left = Node("Mechanics")
root.left.left.right = Node("Optics")

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)

# Preorder traversal
def preorder(root):
    if root:
        print(root.data, end=" -> ")
        preorder(root.left)
        preorder(root.right)

# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" -> ")

print("Library Catalog - Inorder:")
inorder(root)

print("\n\nLibrary Catalog - Preorder:")
preorder(root)

print("\n\nLibrary Catalog - Postorder:")
postorder(root)
