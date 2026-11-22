# Hash Table - Linear Probing With and Without Replacement

SIZE = int(input("Enter hash table size: "))

table = [-1] * SIZE

def hash_function(key):
    return key % SIZE

# Linear probing without replacement
def insert_without_replacement(key):
    index = hash_function(key)

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if table[pos] == -1:
            table[pos] = key
            print(key, "inserted at index", pos)
            return

    print("Hash table is full!")

# Linear probing with replacement
def insert_with_replacement(key):
    index = hash_function(key)

    # If home position is empty
    if table[index] == -1:
        table[index] = key
        print(key, "inserted at index", index)
        return

    # If existing element belongs to another home position
    existing = table[index]

    if hash_function(existing) != index:
        # Place new key in its correct home position
        table[index] = key

        # Reinsert displaced element using linear probing
        start = hash_function(existing)

        for i in range(1, SIZE + 1):
            pos = (start + i) % SIZE

            if table[pos] == -1:
                table[pos] = existing
                print(key, "inserted at index", index)
                print(existing, "displaced to index", pos)
                return

        print("Unable to reinsert displaced element!")
        table[index] = existing
        return

    # If existing element belongs to this home position,
    # insert the new key using linear probing
    for i in range(1, SIZE + 1):
        pos = (index + i) % SIZE

        if table[pos] == -1:
            table[pos] = key
            print(key, "inserted at index", pos)
            return

    print("Hash table is full!")

def display():
    print("\nHash Table:")

    for i in range(SIZE):
        print(i, ":", table[i])

while True:
    print("\n--- Hash Table ---")
    print("1. Insert Without Replacement")
    print("2. Insert With Replacement")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert_without_replacement(key)

    elif choice == 2:
        key = int(input("Enter key: "))
        insert_with_replacement(key)

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice!")
