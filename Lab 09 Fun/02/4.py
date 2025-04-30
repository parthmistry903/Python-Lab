# Write a recursive function that reverses the list of numbers that it receives.
def revList(l):
    if not l:
        return l
    return [l[-1]] + revList(l[:-1])
l=[1,2,3]
print(revList(l))