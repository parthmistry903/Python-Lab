# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies
# inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )
import math

def inOrOutsideOfCircle(r, d):
    return "Inside" if d < r else "On it" if d == r else "Outside"

r = int(input("Enter the radious of circle : "))
x, y = map(
    int,
    input(
        "Give coordinates of point for which u want to check if is it outside or inside circle : "
    ).split(),

)
a, b = map(int, input("Give coordinates of center of circle : ").split())
d = math.sqrt((pow((x - a), 2) + pow((y - b), 2)))
print(inOrOutsideOfCircle(r, d))
