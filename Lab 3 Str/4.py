# Write a function that removes one string from another string, if present.
# E.g. Onestring = "abcdef", removestring = "cd". The finalstring should contain "abef".
def remStr(s, r):
    a = s.replace(r, "")
    return a

s = input("Enter string : ")
r = input("Enter string to remove it from first : ")
print(remStr(s, r))
