# Singly Linked List - Library Catalog

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Book inserted at beginning.")

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

        print("Book inserted at end.")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty!")
        else:
            print("Deleted book:", self.head.data)
            self.head = self.head.next

    # Display list
    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
        else:
            temp = self.head
            print("Library Catalog:")

            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next

            print("None")

ll = LinkedList()

while True:
    print("\n--- Dynamic Library Catalog ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        ll.insert_beginning(book)

    elif choice == 2:
        book = input("Enter book name: ")
        ll.insert_end(book)

    elif choice == 3:
        ll.delete_beginning()

    elif choice == 4:
        ll.display()

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
