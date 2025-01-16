# 1.	Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers
# using random nos. Replace the third element of odd integers with  a list of 4 even integers.
# Flattern, sort and print the list. Provide appropriate message at each stage.
import random

Odd = []
for _ in range(5):
    a = random.randint(1, 100)
    if a % 2 == 0:
        Odd.append(a + 1)
    else:
        Odd.append(a)

print(f"Odd : {Odd}")

Even = []
for _ in range(4):
    a = random.randint(1, 100)
    if a % 2 == 0:
        Even.append(a)
    else:
        Even.append(a + 1)

Odd[2] = Even

Flatten = []
for item in Odd:
    if isinstance(item, list):
        Flatten.extend(item)
    else:
        Flatten.append(item)

print(f"Odd After Adding : {Odd}")
print(f"Even : {Even}")
print(f"Flatten : {Flatten}")

Sort = []
Sort = sorted(Flatten)
print(f"Sort : {Sort}")
