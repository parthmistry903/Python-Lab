#3.	Generate the list of 10 different random numbers between -15 and 15.
#  Create a new list by obtaining square of all numbers in a list.
import random
numbers = [random.randint(-15, 15) for _ in range(10)]
squareList = list(map(lambda x: x**2, numbers))

print(numbers)
print(squareList)