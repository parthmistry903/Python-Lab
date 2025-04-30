# A list contains some negative and some positive values. Write a recursive function
# that sanitizes the list by replacing all negative numbers with 0.
def sanitizeList(l, i=0):
    if i==len(l):       # Can't use if not l
        return
    if l[i] < 0:
        l[i] = 0
    sanitizeList(l, i + 1)  # Be careful when typing [] or ()

l = [1, -3, 2, -2, 4, 5, -6, 6 - 7]
sanitizeList(l)
print(l)
