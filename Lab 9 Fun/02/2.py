# A positive integer is entered through the keyboard. Write a function to find its binary
# equivalent of this number.
def toBinary(n):
    if n == 0:
        return "0"

    binaryDigits = []

    while n > 0:
        binaryDigits.append(str(n % 2))
        n = n // 2

    return "".join(binaryDigits[::-1])

number = 57
binary = toBinary(number)
print(binary)