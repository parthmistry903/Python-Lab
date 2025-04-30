# Accept a number from the user. And print number of digits in it.
def digit(a):
    return len(str(abs(a)))

a = int(input("Enter a no. to check its digit : "))
print(f"No. of digits : {digit(a)}")