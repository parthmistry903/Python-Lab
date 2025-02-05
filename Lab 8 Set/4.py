# A set contains names which begin either with A or with B. Write a program to separate
# out the names into two sets, one containing names beginning with A and another with B.
def separateItems():
    fruits = {"Apple", "Banana", "Apricot", "Blueberry", "Cherry", "Blackberry"}

    aFruits = {fruit for fruit in fruits if fruit.startswith("A")}
    bFruits = {fruit for fruit in fruits if fruit.startswith("B")}

    return aFruits, bFruits

aFruits, bFruits = separateItems()
print("Fruits starting with A:", aFruits)
print("Fruits starting with B:", bFruits)
