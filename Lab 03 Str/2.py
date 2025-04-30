#  Write your own functions (without using built-in functions) to convert all characters of a string
# into lower case/upper case/toggle case.
def toUpper(s):
    a = ""
    for char in s:
        if "a" <= char <= "z":
            a += chr(ord(char) - 32)
        else:
            a += char
    return a


def toLower(s):
    b = ""
    for char in s:
        if "A" <= char <= "Z":
            b += chr(ord(char) + 32)
        else:
            b += char
    return b


def toToggle(s):
    c = ""
    for char in s:
        if "A" <= char <= "Z":
            c += chr(ord(char) + 32)
        elif "a" <= char <= "z":
            c += chr(ord(char) - 32)
        else:
            c += char
    return c

# def toUpper(s):
#     return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in s)

# def toLower(s):
#     return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else char for char in s)

# def toToggle(s):
#     return "".join(chr(ord(char) + 32) if "A" <= char <= "Z" else chr(ord(char) - 32) if "a" <= char <= "z" else char for char in s)

s = input("Enter string : ")
print(f"Uppercase : {toUpper(s)} ; Lowercase : {toLower(s)} ; Togglecase : {toToggle(s)}")
