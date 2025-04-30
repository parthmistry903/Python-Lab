# Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.
class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.params = kwargs
    def surface_area(self):
        if self.shape == "cube":
            a = self.params["side"]
            return 6 * a * a
        elif self.shape == "sphere":
            r = self.params["radius"]
            return 4 * 3.14159 * r * r
    def volume(self):
        if self.shape == "cube":
            a = self.params["side"]
            return a ** 3
        elif self.shape == "sphere":
            r = self.params["radius"]
            return (4/3) * 3.14159 * r ** 3
cube = Solid("cube", side=4)
sphere = Solid("sphere", radius=3)
print(cube.surface_area(), cube.volume())
print(sphere.surface_area(), sphere.volume())