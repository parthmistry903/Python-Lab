# 10. Generate N numbers of Fibonacci series.
N = int(input("Enter N: "))
a, b = 0, 1
for _ in range(N):  # _ is throwaway variable
    print(a, end=" ")
    a, b = b, a + b