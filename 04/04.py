#Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
num = int(input("Enter a number: "))
# Prime
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    print(f"{num} is Prime.")
else:
    print(f"{num} is not Prime.")
# Perfect
if sum(i for i in range(1, num) if num % i == 0) == num:
    print(f"{num} is Perfect.")
else:
    print(f"{num} is not Perfect.")
# Armstrong
if num == sum(int(d) ** len(str(num)) for d in str(num)):
    print(f"{num} is Armstrong.")
else:
    print(f"{num} is not Armstrong.")
# Palindrome
if str(num) == str(num)[::-1]:
    print(f"{num} is Palindrome.")
else:
    print(f"{num} is not Palindrome.")
# Automorphic
if str(num**2).endswith(str(num)):
    print(f"{num} is Automorphic.")
else:
    print(f"{num} is not Automorphic.")
