# A string is entered through the keyboard. Write a recursive function that counts the number 
# of vowels in this string.
def countVowels(s):
    if not s:
        return 0
    vowels = "aeiouAEIOU"
    return (1 if s[0] in vowels else 0) + countVowels(s[1:])

string = "hello world"
print(countVowels(string))

# The print() shows the total number of vowels by adding up the results from each step of 
# the function's recursion. (Total of all return values)
