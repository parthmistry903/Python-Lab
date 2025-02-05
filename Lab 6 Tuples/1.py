# A list contains names of boys and girls as its elements. Boys’ names are stored as tuples.
# Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))
def name(l):
    a, b = 0, 0
    for i in l:
        if isinstance(i, tuple):
            a += len(i)
        else:
            b += 1
    return a, b

l = ["g1", "g2", ("b1", "b2"), "g3", ("b2", "b3", "b4")]
a, b = name(l)
print(f"Boys : {a} ; Girls : {b}")
