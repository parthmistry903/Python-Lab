#Count no. of alphabets and no. of digits in any given string.
text = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
print("Alphabets:", alphabets)
print("Digits:", digits)