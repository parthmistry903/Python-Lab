# A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age.
students = [(101, "Alice", 20), (102, "Bob", 22), (103, "Charlie", 21)]
roll_no = []
names = []
ages = []

for student in students:
    roll_no.append(student[0])
    names.append(student[1])
    ages.append(student[2])

print("Roll Numbers:", roll_no)
print("Names:", names)
print("Ages:", ages)
