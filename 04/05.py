"""Exercise: 05"""
limit = 30; triplets = [(a, b, c) for a in range(1, limit) for b in range(a, limit) for c in range(b, limit) if a**2 + b**2 == c**2]; print(triplets)