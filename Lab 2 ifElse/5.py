#  Accept age of a person. If age is less than 18, print minor otherwise Major.
def ageCheck(a):
    if a < 18:
        return "Minor"
    else:
        return "Major"


age = int(input("Enter your age : "))
print(f"{ageCheck(age)}")
