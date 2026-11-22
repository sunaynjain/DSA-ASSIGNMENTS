# Stack - Library Book Return Management

stack = []

def push(book):
    stack.append(book)
    print(book, "returned and added to stack.")

def pop():
    if len(stack) == 0:
        print("No returned books to process.")
    else:
        print("Processing returned book:", stack.pop())

def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Books in stack (top to bottom):")
        for book in reversed(stack):
            print(book)

while True:
    print("\n--- Library Book Return Management ---")
    print("1. Return Book (Push)")
    print("2. Process Book (Pop)")
    print("3. Display Stack")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        push(book)

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
