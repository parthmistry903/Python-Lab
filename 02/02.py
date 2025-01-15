# Print largest and smallest values out of three.
def largest_smallest(a, b, c):
    largest = max(a, b, c)
    smallest = min(a, b, c)
    return largest, smallest

a, b, c = map(int, input("Enter three numbers separated by space: ").split())
largest, smallest = largest_smallest(a, b, c)
print("Largest:", largest, "Smallest:", smallest)