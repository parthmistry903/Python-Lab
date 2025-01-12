# Problem: Write a menu-driven program to implement the Queue data structure.
from collections import deque
queue = deque()
while True:
    print("1. Enqueue
2. Dequeue
3. Display
4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        element = int(input("Enter the element to enqueue: "))
        queue.append(element)
    elif choice == 2:
        if queue:
            print(f"Dequeued element: {queue.popleft()}")
        else:
            print("Queue is empty.")
    elif choice == 3:
        print(list(queue))
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
