#  Check whether a given number is odd or even.
def OddEven(a):
    return "Even" if a%2==0 else "Odd"

a=int(input("Enter a no. to check is it Even or Odd : "))
print(f"The no. u have entered is {OddEven(a)}")