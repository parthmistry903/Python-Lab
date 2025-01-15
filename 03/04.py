# Write a function that removes one string from another string, if present. 
# E.g. Onestring = "abcdef", removestring = "cd". The finalstring should contain "abef".

def remove_substring(original_string, substring):
    return original_string.replace(substring, '')

onestring = input("Enter the original string: ")
removestring = input("Enter the string to remove: ")
finalstring = remove_substring(onestring, removestring) #finalstring = onestring.replace(removestring, '')
print(f"Final string after removal: {finalstring}")
