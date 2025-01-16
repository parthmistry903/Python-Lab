# Problem: Take two lists of numbers. Create a third list of numbers for only those numbers from the first list which are not there in the second list (use list comprehension).
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 6, 7]
result = [x for x in list1 if x not in list2]
print(result)
#OK
