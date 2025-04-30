# Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.
import csv
students = {}
with open('students.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        rollno, name, maths, physics, chemistry = row
        total = int(maths) + int(physics) + int(chemistry)
        students[int(rollno)] = {
            'name': name,
            'maths': int(maths),
            'physics': int(physics),
            'chemistry': int(chemistry),
            'total': total
        }
for rollno, details in students.items():
    print(f"RollNo: {rollno}, Details: {details}")