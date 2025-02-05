# Write a function to create and return a list containing tuples of the form (x,x^2,x^3)
# for all x between 1 and given ending value (both inclusive).
def listTup(x):
    l = []
    for i in range(1, x + 1):
        l.append((i, i**2, i**3))
    return l

x = int(input())
print(listTup(x))
