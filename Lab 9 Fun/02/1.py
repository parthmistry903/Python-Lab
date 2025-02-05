# If a positive integer is entered through the keyword, write a recursive function to obtain 
# the prime factors of the number. 
def primeFactors(n, i=2):
    if n == 1:
        return
    if n % i == 0:
        print(i, end=" ")
        primeFactors(n // i, i) # a/b will always return a float in Python 3, even if the result is a whole number.
    else:
        primeFactors(n, i + 1 if i == 2 else i + 2)  # Move to next odd number after 2

num = int(input("Enter a number : "))
print("Prime factors:", end=" ")
primeFactors(num)
