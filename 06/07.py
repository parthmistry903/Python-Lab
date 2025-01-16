# Delete an element of a tuple.
# Note: Tuples are immutable, so you cannot delete an element from a tuple directly.
tuple_data = (1, 2, 3, 4)
new_tuple = tuple_data[:2] + tuple_data[3:]

print("Tuple after deletion:", new_tuple)
