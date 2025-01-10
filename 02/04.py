# Check whether a given number is divisible by 10 or not.
def is_divisible_by_10(num):
    return "Divisible by 10" if num % 10 == 0 else "Not divisible by 10"

num = int(input("Enter a number: "))
print(is_divisible_by_10(num))