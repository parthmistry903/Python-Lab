# A palindrome is a word or phrase that reads the same in both directions. Write a program
# that defines a function ispalindrome() which checks whether a given string is a palindrome
# or not. Ignore spaces and case mismatch while checking for palindrome.
def isPalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

s1 = "Madam"
print(isPalindrome(s1))
s2 = "123454321"
print(isPalindrome(s2))
s3 = "A man a plan a canal Panama"
print(isPalindrome(s3))
