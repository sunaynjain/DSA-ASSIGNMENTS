MAX = 25
stack = []

while True:
    print("\n1.Add Report")
    print("2.Review Report")
    print("3.Latest Report")
    print("4.Display Reports")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        no = input("Enter Report Number: ")
        status = input("Enter Status: ")

        if len(stack) == MAX:
            print("Stack Full")

        elif status != "Pending":
            print("Only Pending reports can be added")

        elif any(r[0] == no for r in stack):
            print("Report Number must be unique")

        else:
            stack.append((no, status))

    elif ch == 2:
        if stack:
            print("Reviewed:", stack.pop())
        else:
            print("No Reports")

    elif ch == 3:
        if stack:
            print("Latest Report:", stack[-1])
        else:
            print("No Reports")

    elif ch == 4:
        print(stack)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
