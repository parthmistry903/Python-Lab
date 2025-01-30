def to_lower(s):
    if not s:
        return ""
    c = chr(ord(s[0]) + 32) if 'A' <= s[0] <= 'Z' else s[0]
    return c + to_lower(s[1:])

def to_upper(s):
    if not s:
        return ""
    c = chr(ord(s[0]) - 32) if 'a' <= s[0] <= 'z' else s[0]
    return c + to_upper(s[1:])

def toggle(s):
    if not s:
        return ""
    if 'a' <= s[0] <= 'z':
        c = chr(ord(s[0]) - 32)
    elif 'A' <= s[0] <= 'Z':
        c = chr(ord(s[0]) + 32)
    else:
        c = s[0]
    return c + toggle(s[1:])

u = input("Enter a string: ")
print(f"Lower case: {to_lower(u)}")
print(f"Upper case: {to_upper(u)}")
print(f"Toggle case: {toggle(u)}")
