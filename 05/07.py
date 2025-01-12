# Problem: Write a menu-driven program to implement the stack data structure.
stack = []
while True:
    print("1. Push
2. Pop
3. Display
4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to push: "))
        stack.append(element)
    elif choice == 2:
        if stack:
            print(f"Popped element: {stack.pop()}")
        else:
            print("Stack is empty.")
    elif choice == 3:
        print(stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
