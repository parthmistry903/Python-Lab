# 8. Print factorial of a given number.
def fact():
    from math import factorial
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")

fact()