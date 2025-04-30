facultyNames = ["Alexander", "John", "Catherine", "Elizabeth", "James"]
filteredNames = list(filter(lambda name: len(name) > 8, facultyNames))
print(filteredNames)