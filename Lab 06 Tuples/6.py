# Modify an element of a tuple.
def modifyTup(t):
    print("Original tuple:", t)
    i = int(input("Enter the index to modify: "))
    v = int(input("Enter the new value: "))
    l = list(t)
    l[i] = v
    return tuple(l)

result = modifyTup((1, 2, 3, 4))
print("Modified tuple:", result)
