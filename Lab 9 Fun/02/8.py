# Write a recursive function to obtain length of a given string.
# Method 1
def strLenMethod_1(s):
    if s == "":
        return 0
    return 1 + strLenMethod_1(s[1:])            # (1 + ...) imp

# Method 2
def Method_2(s, length=0, index=0):
    if index == len(s):
        return length
    return Method_2(s, length + 1, index + 1)

s = "abc"
print(Method_2(s))
print(strLenMethod_1(s))