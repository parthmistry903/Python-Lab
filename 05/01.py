# Problem: Create a list of 5 odd integers using random nos. Similarly, create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flatten, sort, and print the list. Provide appropriate message at each stage.
import random
odd = random.sample(range(1, 100, 2), 5)
even = random.sample(range(2, 100, 2), 4)
odd[2] = even
flat_list = sorted([x for sublist in odd for x in (sublist if isinstance(sublist, list) else [sublist])])
print(flat_list)
