# Check whether a given number is odd or even.
def check_odd_even(num):
    return "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print(check_odd_even(num))