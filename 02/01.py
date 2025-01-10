# Print largest and smallest values out of two.
def largest_smallest_two(a, b):
    largest = a if a > b else b
    smallest = a if a < b else b
    return largest, smallest

a, b = map(int, input("Enter two numbers separated by space: ").split())
largest, smallest = largest_smallest_two(a, b)
print("Largest:", largest, "Smallest:", smallest)