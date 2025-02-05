# 2.	Generate 20 random integers and store them in a list. Accept a number from the user
# and print position of all occurrences of that number in the list.
import random

list = []
for _ in range(20):
    a = random.randint(1, 100)
    list.append(a)

print(f"List: {list}")
b = int(input("Enter a number u want to know position: "))

n_list = []
for i in range(20):
    if list[i] == b:
        n_list.append(i)

print(f"Here's index positions: {n_list}")