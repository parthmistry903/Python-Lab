# Accept two strings. Check whether one string is there in another string.
def isSubstr(str1, str2):
    return str2 in str1

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if isSubstr(str1, str2):
    print(f"'{str2}' is present in '{str1}'.")
else:
    print(f"'{str2}' is not present in '{str1}'.")
