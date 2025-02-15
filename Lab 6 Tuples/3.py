# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find
# the number of days between the two dates.
def isLeap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def daysInM(m, y):
    d = [31, 28 + isLeap(y), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    return d[m - 1]


def daysFrom0(date):
    d, m, y = date
    day = d
    for i in range(1, m):
        day += daysInM(m, y)
    day += y * 365 + y // 4 - y // 100 + y // 400
    return day


date1 = (5, 1, 2024)
date2 = (2, 1, 2024)
print(abs(daysFrom0(date2) - daysFrom0(date1)))
y = 2025