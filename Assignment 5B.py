# Student Admission Record Management using BST

class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.left = None
        self.right = None

def insert(root, roll, name):
    if root is None:
        return Node(roll, name)

    if roll < root.roll:
        root.left = insert(root.left, roll, name)

    elif roll > root.roll:
        root.right = insert(root.right, roll, name)

    else:
        print("Roll number already exists!")

    return root

def search(root, roll):
    if root is None:
        return None

    if roll == root.roll:
        return root

    elif roll < root.roll:
        return search(root.left, roll)

    else:
        return search(root.right, roll)

def inorder(root):
    if root:
        inorder(root.left)
        print("Roll No:", root.roll, "| Name:", root.name)
        inorder(root.right)

root = None

while True:
    print("\n--- Student Admission System ---")
    print("1. Insert Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        root = insert(root, roll, name)

    elif choice == 2:
        roll = int(input("Enter roll number to search: "))
        result = search(root, roll)

        if result:
            print("Student Found!")
            print("Roll Number:", result.roll)
            print("Name:", result.name)
        else:
            print("Student not found.")

    elif choice == 3:
        print("\nStudent Records in Sorted Order:")
        inorder(root)

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
