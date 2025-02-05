# Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
def isprime(n):
    if n <= 1:
        print("Not prime")
        return
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            print("Not prime")
            return
    print("Prime")

def isperfect(n):
    if sum(i for i in range(1, n) if n % i == 0) == n:
        print("Perfect")
    else:
        print("Not Perfect")

def isArmstrong(n):
    if sum(int(char) ** int(len(str(n))) for char in str(n)) == n:
        print("Armstrong")
    else:
        print("Not Armstrong")

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

def isAutomorphic(n):
    sq = n * n
    if str(sq).endswith(str(n)):
        print("Automorphic")
    else:
        print("Not Automorphic")

n = int(input("Enter a no. : "))

isprime(n)
isperfect(n)
isArmstrong(n)
isPalindrome(n)
isAutomorphic(n)