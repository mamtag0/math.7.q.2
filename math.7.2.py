import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Function for sin(x)
def f(x):
    return np.sin(x)

# Function for the line from (0,0) to (7π/6, -1/2)
def g(x):
    return (-1/2) / ((7 * np.pi) / 6) * x  # Simplified slope * x

# Difference between the functions: f(x) - g(x)
def area_between(x):
    return f(x) - g(x)

# Integration limits
a = 0
b = (7 * np.pi) / 6

# 1. Definite Integral Method
area_integral, _ = quad(area_between, a, b)
print("Area using definite integral:", area_integral)

# 2. Monte Carlo Simulation
np.random.seed(0)
N = 10000  # You can increase for more accuracy

x_rand = np.random.uniform(a, b, N)
y_min = min(g(x_rand))
y_max = max(f(x_rand))
y_rand = np.random.uniform(y_min, y_max, N)

# Count how many random points fall between the two curves
y_upper = f(x_rand)
y_lower = g(x_rand)
points_inside = (y_rand < y_upper) & (y_rand > y_lower)

# Area of bounding rectangle
area_rect = (b - a) * (y_max - y_min)
area_monte_carlo = area_rect * np.sum(points_inside) / N

print("Area using Monte Carlo simulation:", area_monte_carlo)

# Optional: Plot
x_vals = np.linspace(a, b, 500)
plt.plot(x_vals, f(x_vals), label='y = sin(x)')
plt.plot(x_vals, g(x_vals), label='line from (0,0) to (7π/6, -1/2)', linestyle='--')
plt.fill_between(x_vals, f(x_vals), g(x_vals), where=(f(x_vals) > g(x_vals)), alpha=0.3, color='purple')
plt.legend()
plt.title("Area Between Curves")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
