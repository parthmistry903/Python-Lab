# Implement a String class containing the following functions: a. Overloaded += operator function to perform string concatenation b. Method toLower() to convert upper case letters to lower case. c. Method toUpper() to convert lower case letters to upper case.
class String:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, other):
        self.value += other.value
        return self
    def toLower(self):
        self.value = self.value.lower()
        return self
    def toUpper(self):
        self.value = self.value.upper()
        return self
    def display(self):
        print(self.value)
s1 = String("Hello ")
s2 = String("World")
s1 += s2
s1.display()
s1.toLower().display()
s1.toUpper().display()