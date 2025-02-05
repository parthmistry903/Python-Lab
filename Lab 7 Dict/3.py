# Create a dictionary with dept no, employee roll no. and salary.
# Find out department wise min and maximum of salary.
def findMinMaxSalary(deptInfo):
    for dept, info in deptInfo.items():
        minS = min(info["Salary"])
        maxS = max(info["Salary"])
        print(f"Department {dept} - Min Salary: {minS}, Max Salary: {maxS}")

deptInfo = {
    101: {"empRollNo": [1001, 1002, 1003], "Salary": [50000, 55000, 60000]},
    102: {"empRollNo": [2001, 2002, 2003], "Salary": [45000, 47000, 52000]},
    103: {"empRollNo": [3001, 3002, 3003], "Salary": [60000, 62000, 68000]},
}

findMinMaxSalary(deptInfo)
