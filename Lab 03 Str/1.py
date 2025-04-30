#  Count how many vowels are there in a string. Accept the string from the user.
def vowelCheck(str):
    count = (
        str.count("a")
        + str.count("e")
        + str.count("i")
        + str.count("o")
        + str.count("u")
        + str.count("A")
        + str.count("E")
        + str.count("I")
        + str.count("O")
        + str.count("U")
    )
    # vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    # return sum(1 for char in str if char in vowels)
    return count

a = input("Enter a string to check how many vowels are there in it : ")
print(vowelCheck(a))
