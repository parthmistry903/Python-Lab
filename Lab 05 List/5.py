# 5.	A list contains 5 strings. Convert all these strings to uppercase.
list = ["apple", "banana", "mango", "watermelon", "chikoo"]
print(f"List: {list}")

cap = [s.upper() for s in list]
print(f"Capitalized Strings: {cap}")

#Or upper_case_string += chr(ord(char) - 32)