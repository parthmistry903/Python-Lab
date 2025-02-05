#  Print largest and smallest values out of three.
def larSmaOutOf3(a, b, c):
    
    # l = max(a, b, c) 
    # s = min(a, b, c)

    if a >= b and a >= c:
        l = a
    elif b >= a and b >= c:
        l = b
    else:
        l = c

    if a <= b and a <= c:
        s = a
    elif b <= a and b <= c:
        s = b
    else:
        s = c

    return l, s


a, b, c = map(int, input("Enter 3 numbers seperated by space :").split())
l, s = larSmaOutOf3(a, b, c)
print(f"Largest : {l} , Smallest : {s}")
