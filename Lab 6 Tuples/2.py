# A list contains tuples containing roll no., name and age of student. Write a python program
# to create three lists separately for roll no., name and age.
def sepList(l, roll, name, age):
    for i in l:
        roll.append(i[0])
        name.append(i[1])
        age.append(i[2])
    print(roll)
    print(name)
    print(age)

l = [(1, "a", 18), (2, "b", 17), (3, "c", 19)]
roll = []
name = []
age = []
sepList(l, roll, name, age)
