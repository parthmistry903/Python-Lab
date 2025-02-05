# 9.	Take two lists of numbers. Create third list of numbers for only those numbers from first
#  list which are not there in 2nd list (use list comprehension).
list1 = [int(x) for x in input("Enter numbers for the first list (separated by spaces): ").split()]
list2 = [int(x) for x in input("Enter numbers for the second list (separated by spaces): ").split()]

list3 = [n for n in list1 if n not in list2]

print("First list:", list1)
print("Second list:", list2)
print("Numbers in the first list not in the second list:", list3)
