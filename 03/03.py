#Accept two strings. Check whether one string is there in another string.
def is_substring(string1, string2):
    return string2 in string1

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if is_substring(string1, string2):
    print(f"'{string2}' is present in '{string1}'.")
else:
    print(f"'{string2}' is not present in '{string1}'.")
