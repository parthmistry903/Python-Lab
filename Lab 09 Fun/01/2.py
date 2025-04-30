# Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn,
# where n is digit received by the function. test the function for digits 4 to 7.
def compute(n):
    num1 = n
    num2 = int(str(n) * 2)
    num3 = int(str(n) * 3)
    num4 = int(str(n) * 4)
    total = num1 + num2 + num3 + num4
    return total

print(compute(4))
print(compute(5))
print(compute(6))
print(compute(7))

# for i in range(4, 8):
#     print(compute(i))