# 11. Calculate sin(x); x is a radian value.
from math import factorial, pi

def sin_x(x):
    sin_x = 0
    for n in range(10):
        term = (-1)**n * (x**(2*n + 1)) / factorial(2*n + 1)
        sin_x += term
    return sin_x

x = float(input("Enter x in degrees: ")) * pi / 180
print(f"sin({x}) = {sin_x(x)}")
