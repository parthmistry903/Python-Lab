# Problem: Generate 20 random integers and store them in a list. Accept a number from the user and print the position of all occurrences of that number in the list.
import random
nums = [random.randint(1, 50) for _ in range(20)]
num = int(input("Enter a number: "))
positions = [i for i, x in enumerate(nums) if x == num]
print(positions)
