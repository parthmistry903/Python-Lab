#  Write a program that defines a function count_lower_upper() that accepts a string and calculates
#  the number of uppercase and lowercase alphabets in it. It should return these values as
#  a dictionary. Call this function for some sample string.
def countLowerUpper(s):
    d = {"uppercase": 0, "lowercase": 0}
    for char in s:
        if char.isupper():
            d["uppercase"] += 1
        elif char.islower():
            d["lowercase"] += 1
    return d

s = "aBcDEF"
print(countLowerUpper(s))
