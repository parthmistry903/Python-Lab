# Remove empty tuple(s) from the list of tuples.
def removeEmptyTupFromList(l):
    return [i for i in l if i]

l = [(1, 2, 3), (), (4, 5), (), (6, 7, 8), ()]
print(removeEmptyTupFromList(l))
