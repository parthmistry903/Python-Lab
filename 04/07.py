# 7. Print nCr and nPr.
from math import factorial
n = int(input("Enter n: "))
r = int(input("Enter r: "))
nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)
print(f"nCr = {nCr}")
print(f"nPr = {nPr}")

# OR
# import math
# n = int(input("Enter n: "))
# r = int(input("Enter r: "))
# nCr = math.comb(n, r)  # Combination: nCr = n! / (r! * (n-r)!)
# nPr = math.perm(n, r)  # Permutation: nPr = n! / (n-r)!
# print(f"nCr: {nCr}")
# print(f"nPr: {nPr}")