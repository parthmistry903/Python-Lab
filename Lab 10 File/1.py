# Write a program to create a csv file that we can directly open in MS-Excel.
import csv
data = [
    ['RollNo', 'Name', 'Maths', 'Physics', 'Chemistry'],
    [1, 'Alice', 85, 90, 88],
    [2, 'Bob', 78, 82, 80],
    [3, 'Charlie', 92, 95, 89]
]
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)