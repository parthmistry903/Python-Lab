# Write a program that creates and uses a Time class to perform various time arithmetic operations.
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()
    def normalize(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
    def __add__(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )
    def __sub__(self, other):
        total1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        total2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff = total1 - total2
        return Time(diff // 3600, (diff % 3600) // 60, diff % 60)
    def display(self):
        print(f"{self.hours}:{self.minutes:02d}:{self.seconds:02d}")
t1 = Time(2, 45, 30)
t2 = Time(1, 30, 45)
(t1 + t2).display()
(t1 - t2).display()