# Print largest and smallest values out of two.
def largestAndSmallest(a, b):
    if a > b:
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a
    return largest, smallest

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

largest, smallest = largestAndSmallest(a, b)
print(f"Largest = {largest} , Smallest = {smallest}")
