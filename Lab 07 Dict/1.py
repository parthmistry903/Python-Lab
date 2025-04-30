#  Write a program to create three dictionaries and concatenate them to create fourth dictionary.
def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

dict4 = concatenate_dicts(dict1, dict2, dict3)
print(dict4)

# dict4 = {**dict1, **dict2, **dict3}  # For new version of py
