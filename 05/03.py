# Problem: Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random
nums = list(set(random.randint(1, 30) for _ in range(50)))
print(nums)
