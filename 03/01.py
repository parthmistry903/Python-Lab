#Count how many vowels are there in a string. Accept the string from the user.
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(user_input)}")
