# Write a program that defines a function count_alpha_digits() that accepts a string and calculates
# the number of alphabets and digits in it. It should return these values as a dictionary
def countAlphaDigits(s):
    countA = 0
    countD = 0
    for i in s:
        if i.isdigit():             # Don't use isinstance here !
            countD += 1
        elif i.isalpha():
            countA += 1
    d = {"Alphas": countA, "Digits": countD}
    return d

s = "123abc4defghi5"
print(countAlphaDigits(s))

# isinstance('123', int)  # False, because '123' is a string, not an integer
# '123'.isdigit()  # True, because '123' consists only of digits