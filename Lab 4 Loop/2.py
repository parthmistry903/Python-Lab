#  Print a multiplication table of a given number.
def printTable(i):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

i = int(input("Enter a number to print its table : "))
printTable(i)
