# Calculate a^b where a and b received through the keyword using recursion.
def power(a, b):
    if b == 0:
        return 1
    # if b % 2 == 0:                    # This 3 lines method make code efficiency (Time complexity concept)
    #     halfPower = power(a, b // 2)
    #     return halfPower * halfPower
    return a * power(a, b - 1)  # It pauses here until the next recursive call finishes.

print(power(2, 3))
