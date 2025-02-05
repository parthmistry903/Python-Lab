# Write a program that reads a string from the keyboard and creates dictionary containing 
# frequency of each character occurring in the string. 
def countChar_Frequency(str):
    d = {}
    for ch in str:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d

str = input("Enter a string: ")
print(countChar_Frequency(str))
