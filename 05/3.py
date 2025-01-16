# 3.	Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random

list = []
for _ in range(50):
    c = random.randint(1, 30)
    list.append(c)
print(list)

sort = []
for i in list:
    if i not in sort:
        sort.append(i)
print(sort)