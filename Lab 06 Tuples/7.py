#  Delete an element of a tuple.
def delElement(t):
    print("Original tuple:", t)
    i = int(input("Enter the index to delete: "))
    l = list(t)
    del l[i]
    return tuple(l)

result = delElement((1, 2, 3, 4))
print("Modified tuple:", result)
