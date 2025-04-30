# Accept a year value from the user. Check whether it is a leap year or not.
def leapYrCheck(y):
    if y % 400 == 0:
        return 1
    elif y % 100 == 0:
        return 0
    elif y % 4 == 0:
        return 1
    else:
        return 0

y = int(input("Enter year to check is it leap or not : "))
if leapYrCheck(y):
    print("Leap year")
else:
    print("Non leap year")
