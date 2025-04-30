# Write a program to create a set containing 10 random numbers in the range 15 to 45.
# Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
import random

def processNums():
    nums = set()
    while len(nums) < 10:  # Don't use <= 10
        nums.add(random.randint(15, 45))

    count = 0
    filtNums = set()
    for num in nums:
        if num < 30:
            count += 1
        if num <= 35:
            filtNums.add(num)

    return nums, count, filtNums

nums, count, filtNums = processNums()
print(f"Generated: {nums}")
print(f"Less than 30: {count}")
print(f"Less than or equal to 35: {filtNums}")

# no! : nums = {random.randint(15, 45) for _ in range(10)}  # Don't use this (only) bcz it auto delete duplicates