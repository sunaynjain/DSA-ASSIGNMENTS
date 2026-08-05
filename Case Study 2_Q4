MAX = 30
queue = []

while True:
    print("\n1.Add Print Job")
    print("2.Print Job")
    print("3.View Next Job")
    print("4.Display Print Queue")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        job_id = input("Enter Job ID: ")
        file_type = input("Enter File Type (PDF/DOCX): ")

        if len(queue) == MAX:
            print("Queue Full")

        elif file_type not in ["PDF", "DOCX"]:
            print("Invalid File Type")

        elif any(job[0] == job_id for job in queue):
            print("Duplicate Job ID")

        else:
            queue.append((job_id, file_type))

    elif ch == 2:
        if queue:
            print("Printed:", queue.pop(0))
        else:
            print("Queue Empty")

    elif ch == 3:
        if queue:
            print("Next Job:", queue[0])
        else:
            print("Queue Empty")

    elif ch == 4:
        print(queue)

    elif ch == 5:
        break

    else:
        print("Invalid Choice")
