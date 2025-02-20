# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find
# the number of days between the two dates.
def isLeap(y):
    return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

def daysInM(m, y):
    l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and isLeap(y):
        return 29
    return l[m - 1]

def final(dt1, dt2):
    d1, m1, y1 = dt1
    d2, m2, y2 = dt2
    c = 0
    while y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 < d2):
        c += 1
        d1 += 1
        if d1 > daysInM(m1, y1):
            d1 = 1
            m1 += 1
        if m1 > 12:
            m1 = 1
            y1 += 1
    return c

dt1 = (2, 4, 2007)
dt2 = (20, 2, 2025)
print(final(dt1, dt2))