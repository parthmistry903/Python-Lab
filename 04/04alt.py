def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

def is_armstrong(num):
    total = 0
    power = len(str(num))
    for d in str(num):
        total += int(d) ** power
    return total == num

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is Prime.")
else:
    print(num, "is not Prime.")

if is_perfect(num):
    print(num, "is Perfect.")
else:
    print(num, "is not Perfect.")

if is_armstrong(num):
    print(num, "is Armstrong.")
else:
    print(num, "is not Armstrong.")

if is_palindrome(num):
    print(num, "is Palindrome.")
else:
    print(num, "is not Palindrome.")

if is_automorphic(num):
    print(num, "is Automorphic.")
else:
    print(num, "is not Automorphic.")
