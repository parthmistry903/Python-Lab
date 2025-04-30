# Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.
class Shape:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.params = kwargs
    def perimeter(self):
        if self.shape == "circle":
            r = self.params["radius"]
            return 2 * 3.14159 * r
        elif self.shape == "square":
            a = self.params["side"]
            return 4 * a
    def area(self):
        if self.shape == "circle":
            r = self.params["radius"]
            return 3.14159 * r * r
        elif self.shape == "square":
            a = self.params["side"]
            return a * a
circle = Shape("circle", radius=5)
square = Shape("square", side=4)
print(circle.perimeter(), circle.area())
print(square.perimeter(), square.area())