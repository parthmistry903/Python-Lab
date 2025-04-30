# Write a program to create a csv file that we can directly open in MS-Excel.
data = [
    ['RollNo', 'Name', 'Maths', 'Physics', 'Chemistry'],
    [1, 'A', 85, 90, 88],
    [2, 'B', 78, 82, 80],
    [3, 'C', 92, 95, 89]
]

with open('students.csv', 'w', newline='') as f:
    for row in data:
        line = ','.join(str(item) for item in row)
        f.write(line + '\n')
