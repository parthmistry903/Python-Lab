# Remove empty tuple(s) from the list of tuples.
tuple_list = [(), ("a", 1), (), ("b", 2), ("c", 3), ()]
tuple_list = [t for t in tuple_list if t]

print("List after removing empty tuples:", tuple_list)
