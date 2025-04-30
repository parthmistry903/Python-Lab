# Count no. of alphabets and no. of digits in any given string.
def adt():
    alphabets = sum(c.isalpha() for c in text)
    digits = sum(c.isdigit() for c in text)
    return alphabets, digits

text = input("Enter a string: ")
a, d = adt()
print("Alphabets:", a)
print("Digits:", d)