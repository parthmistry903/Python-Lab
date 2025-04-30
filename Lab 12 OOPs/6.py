# Write a program to create a class Date that has a list containing day, month and year attributes. Define an overloaded == operator to compare two Date objects.
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]
    def __eq__(self, other):
        return self.date == other.date
    def display(self):
        print(f"{self.date[0]}/{self.date[1]}/{self.date[2]}")
d1 = Date(15, 8, 2023)
d2 = Date(15, 8, 2023)
d3 = Date(16, 8, 2023)
print(d1 == d2)
print(d1 == d3)