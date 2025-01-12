"""Exercise: 03"""
string = 'Hello123'; alphabets = sum(c.isalpha() for c in string); digits = sum(c.isdigit() for c in string); print(f'Alphabets: {alphabets}, Digits: {digits}')