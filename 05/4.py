# 4.	Generate 30 random numbers and put them in a list. Create two more lists – one containing
# only +ve numbers and another with –ve nos.
import random

list = []
for _ in range(30):
    a = random.randint(-50, 50)
    list.append(a)
print(list)
posi = []
nege = []
for i in list:
    if i > 0:
        posi.append(i)
    elif i < 0:
        nege.append(i)
print(posi)
print(nege)
