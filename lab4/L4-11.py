import math

x_deg = 30
x = x_deg * 3.14159 / 180  # Radians
terms = 10
sin_x = 0
for i in range(terms):
    sign = (-1) ** i
    sin_x += sign * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
print("sin(x):", sin_x)
