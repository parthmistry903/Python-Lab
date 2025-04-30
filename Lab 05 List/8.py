# 8.	Write a menu-driven program to implement the Queue data structure.
queue = []

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        queue.append(input("Enter item: "))
    elif choice == "2":
        print("Dequeued:", queue.pop(0) if queue else "Queue is empty!")
    elif choice == "3":
        print("Queue:", queue if queue else "Queue is empty!")
    elif choice == "4":
        break
    else:
        print("Invalid choice, try again!")
