MAX = 80
queue = []

while True:
    print("\n1.Add Call")
    print("2.Answer Call")
    print("3.View Next Call")
    print("4.Display Call Queue")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        call_id = input("Enter Call ID: ")
        status = input("Enter Call Status: ")

        if len(queue) == MAX:
            print("Queue Full")

        elif status != "Active":
            print("Only Active calls are accepted")

        elif any(call[0] == call_id for call in queue):
            print("Duplicate Call ID")

        else:
            queue.append((call_id, status))

    elif ch == 2:
        if queue:
            print("Answered Call:", queue.pop(0))
        else:
            print("Queue Empty")

    elif ch == 3:
        if queue:
            print("Next Call:", queue[0])
        else:
            print("Queue Empty")

    elif ch == 4:
        print(queue)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
