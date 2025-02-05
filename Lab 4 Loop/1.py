#  Print all alphabets in upper case and in lower case
def alf():
    u = "".join((chr(i)) for i in range(65, 91))
    l = "".join((chr(i)) for i in range(97, 123))
    return u, l

u, l = alf()
print(f"Uppercase : {u} ; \nLowercase : {l}")
