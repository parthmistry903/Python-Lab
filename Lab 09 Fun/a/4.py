#4.	Consider the following list:
#lst = ['madam','Python',"malayalam",12321]
#Write a program to print those strings which are palindromes.
lst = ['madam', 'Python', "malayalam", 12321]
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], lst))
print(palindromes)