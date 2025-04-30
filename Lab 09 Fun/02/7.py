# Write a recursive function to obtain average of all numbers present in a given list.
def calculateAverage(l, index=0, total=0, count=0):
    if index == len(l):
        if count == 0:
            return 0
        return total / count
    return calculateAverage(l, index + 1, total + l[index], count + 1)

l = [1, 5, 7, 7, 4, 5, 8, 6, 7]
avg = calculateAverage(l)
print(f"Average : {avg:.2f}")  # print(f"Average : {round(avg,2)}")         