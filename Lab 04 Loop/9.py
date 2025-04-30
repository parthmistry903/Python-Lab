# 9. Print N natural numbers in reverse.
def nrev(N):
    for i in range(N, 0, -1):
        print(i, end=" ")

N = int(input("Enter N: "))
nrev(N)