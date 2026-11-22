# Queue - Ticket Booking Counter

queue = []
MAX_SIZE = 5

def enqueue(customer):
    if len(queue) == MAX_SIZE:
        print("Queue is full!")
    else:
        queue.append(customer)
        print(customer, "added to queue.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        customer = queue.pop(0)
        print("Ticket booked for:", customer)

def display():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("Customers in queue:")
        for customer in queue:
            print(customer)

while True:
    print("\n--- Ticket Booking Counter ---")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        enqueue(name)

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
