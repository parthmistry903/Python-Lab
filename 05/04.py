# Problem: Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve numbers.
import random
nums = [random.randint(-50, 50) for _ in range(30)]
positive = [x for x in nums if x > 0]
negative = [x for x in nums if x < 0]
print(positive, negative)
