import random
numbers = [random.randint(-15, 15) for _ in range(10)]
squareList = list(map(lambda x: x**2, numbers))

print(numbers)
print(squareList)