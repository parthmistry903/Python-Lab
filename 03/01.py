#Count how many vowels are there in a string. Accept the string from the user without loop.
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    return sum(vowels.count(vowels))

user_input = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(user_input)}")
