#  Check whether a triangle is valid or not, when the three angles of the triangle are entered
# through the keyboard. A triangle is valid if te sum of all the three angles is equal to 180 degrees.
def validTri(s):
    return "Valid Triangle" if s == 180 else "Invalid Triangle"

a, b, c = map(int, input("Enter the angles of triangle : ").split())
s = a + b + c
print(validTri(s))
