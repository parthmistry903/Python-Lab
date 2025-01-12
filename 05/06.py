# Problem: Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
fahrenheit = [32, 212, 98.6, 104, 50]
celsius = [(f - 32) * 5/9 for f in fahrenheit]
print(celsius)
