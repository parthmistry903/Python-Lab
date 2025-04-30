# 7.	Write a menu-driven program to implement the stack data structure.
# Initialize an empty stack
stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        stack.append(input("Enter item: "))
    elif choice == "2":
        print("Popped:", stack.pop() if stack else "Stack is empty!")
    elif choice == "3":
        print("Stack:", stack if stack else "Stack is empty!")
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again!")
