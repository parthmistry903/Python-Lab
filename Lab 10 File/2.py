# Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.
students = {}

with open('students.csv', 'r') as f:
    lines = f.readlines()

for line in lines[1:]:
    line = line.strip()
    row = line.split(',')

    rollno = int(row[0])
    name = row[1]
    maths = int(row[2])
    physics = int(row[3])
    chemistry = int(row[4])

    total = maths + physics + chemistry

    students[rollno] = {
        'name': name,
        'maths': maths,
        'physics': physics,
        'chemistry': chemistry,
        'total': total
    }

for rollno, details in students.items():
    print(f"RollNo: {rollno}, Details: {details}")