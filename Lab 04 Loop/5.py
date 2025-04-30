#  Generate all Pythagorean Triplets with side length <= 30.
def pythaTri():
    for a in range(1,31):
        for b in range(a,31):
            for c in range(b,31):
                if a**2 + b**2 == c**2:
                    print(f"{a} {b} {c}")

pythaTri()