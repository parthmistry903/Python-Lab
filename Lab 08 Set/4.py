# A set contains names which begin either with A or with B. Write a program to separate
# out the names into two sets, one containing names beginning with A and another with B.
def separateItems():
    fs = {"Apple", "Banana", "Apricot", "Blueberry", "Cherry", "Blackberry"}

    aFs = {f for f in fs if f.startswith("A")}
    bFs = {f for f in fs if f.startswith("B")}

    return aFs, bFs

aFs, bFs = separateItems()
print("Fruits starting with A:", aFs)
print("Fruits starting with B:", bFs)
