# A list contains names of boys and girls as its elements. Boys' names are stored as tuples. Write a program to find out number of boys and girls in the list.
boys_and_girls = [("John", "Mike"), "Alice", ("Tom", "Jim"), "Sara", "Rachel", ("David", "Sam")]
boys = 0
girls = 0

for ele in boys_and_girls:
    if isinstance(ele, tuple):
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)
