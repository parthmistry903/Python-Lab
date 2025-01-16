# Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.
from datetime import date

date1 = (15, 1, 2025)
date2 = (16, 1, 2025)

d1 = date(date1[2], date1[1], date1[0])
d2 = date(date2[2], date2[1], date2[0])

difference = (d2 - d1).days

print("Number of days between the two dates:", difference)
