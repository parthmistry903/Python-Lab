# Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether
# a given string is pangram or not, through a user-defined function ispangram(). Test the function
# with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite
#  opal jewels”. Hint: use set() to convert the string into a set of characters present in the
#  string and use <= to check whether alphaset is a subset of the given string.
def isPangram(string):
    setAlphas = set("abcdefghijklmnopqrstuvwxyz")
    setStr = set(string.lower())
    return setAlphas <= setStr

string1 = "The quick brown fox jumps over the lazy dog"
string2 = "Crazy Fredrick bought many very exquisite opal jewels"

print(isPangram(string1))
print(isPangram(string2))
