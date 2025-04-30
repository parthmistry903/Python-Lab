# Create an empty set. Write a program that adds five new names to this set, modifies one existing
# name and deletes two names from it. 
def modifySet():
    names = set()
    for _ in range(5):
        name = input("Enter a name: ")
        names.add(name)
    
    names.remove(input("Enter a name to modify: "))
    names.add(input("Enter the new name: "))
    
    names.discard(input("Enter a name to delete: "))
    names.discard(input("Enter another name to delete: "))
    
    return names

names = modifySet()
print(names)