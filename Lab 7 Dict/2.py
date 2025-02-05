# Write a program to check whether a dictionary is empty or not.
def checkEmpty(d):
    if not d:
        return "Empty"
    else:
        return "Not Empty"

myDict = {}
result = checkEmpty(myDict)
print(result)
