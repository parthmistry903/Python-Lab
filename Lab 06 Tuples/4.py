# Create a list of tuples containing a food item and its price.
# Sort the tuples in descending order by price.
def tupSortDes(l):
    l1 = []
    l1 = sorted(l, key=lambda x: x[1], reverse=True) #reverse=True: Sorts in descending order.
    return l1

l = [("a", 100), ("b", 150), ("c", 200)]
print(tupSortDes(l))
