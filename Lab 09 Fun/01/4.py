# Write a program that defines a function sum_avg() to accept marks of five subjects and calculates
# total and average. It should return  directly both values.
def sumAvg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = [80, 75, 90, 85, 88]
total, average = sumAvg(marks)
print(f"Total: {total}, Average: {average}")