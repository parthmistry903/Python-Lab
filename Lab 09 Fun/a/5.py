#5.	A list contains names of Faculty Members. Write a program to filter out those names
#  whose length is more than 8 characters.
facultyNames = ["abcdefghi", "abcd", "abcdefgh", "abcdefg", "abcdefghijklmn"]
filteredNames = list(filter(lambda name: len(name) > 8, facultyNames))
print(filteredNames)