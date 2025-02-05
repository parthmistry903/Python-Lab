# 6.	Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
fahrenheit_temps = [32, 45, 50, 72, 100]

celsius_temps = [(f - 32) * 5 / 9 for f in fahrenheit_temps]
print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Equivalent temperatures in Celsius:", celsius_temps)
