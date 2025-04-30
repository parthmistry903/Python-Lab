# Generate N numbers of Fibonacci series.
def fib(N):
    a, b = 0, 1
    for _ in range(N):
        print(a, end=" ")
        a, b = b, a + b

N = int(input("Enter N (for which till Fibonacci series printed) : "))
fib(N)
