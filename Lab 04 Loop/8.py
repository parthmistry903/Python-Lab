# Print factorial of a given number.
from math import factorial

def fact():
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial(num)}")

fact()