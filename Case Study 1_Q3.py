MAX = 25
stack = []


def push(action):
    if action not in ["Insert", "Delete", "Replace"]:
        print("Invalid Action")
        return

    if len(stack) > 0 and stack[-1] == action:
        print("Duplicate Action Ignored")
        return

    if len(stack) == MAX:
        print("Stack Full")
        return

    stack.append(action)


def pop():
    if len(stack) == 0:
        print("No Action to Undo")
    else:
        print("Undo:", stack.pop())


def peek():
    if len(stack) == 0:
        print("No Actions")
    else:
        print("Last Action:", stack[-1])


def display():
    if len(stack) == 0:
        print("Action Stack is Empty")
    else:
        print("Action Stack:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])
push("Insert")
push("Delete")
push("Delete")
push("Replace")
push("Copy") 

display()

peek()

pop()

display()
