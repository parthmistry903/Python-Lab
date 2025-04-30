# If an Employee object contains following details: empcode, empname, Date of Joining, Salary. Write a program to serialize and deserialize this data.
import json
employee = {
    'empcode': 'E001',
    'empname': 'John Doe',
    'doj': '2023-01-15',
    'salary': 50000
}
with open('employee.json', 'w') as f:
    json.dump(employee, f)
with open('employee.json', 'r') as f:
    emp_data = json.load(f)
print(emp_data)