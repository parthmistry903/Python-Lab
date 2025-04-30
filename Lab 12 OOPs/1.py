# Write a program to create a class that represents Complex numbers containing real and imaginary parts and then use it to perform complex number addition, subtraction, multiplication and division.
class Complex:
    def __init__(self, r=0.0, i=0.0):
        self.real = r
        self.imag = i
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real
        )
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        return Complex(
            (self.real * other.real + self.imag * other.imag) / denom,
            (self.imag * other.real - self.real * other.imag) / denom
        )
    def display(self):
        print(f"{self.real} + {self.imag}i")
c1 = Complex(3, 2)
c2 = Complex(1, 7)
(c1 + c2).display()
(c1 - c2).display()
(c1 * c2).display()
(c1 / c2).display()