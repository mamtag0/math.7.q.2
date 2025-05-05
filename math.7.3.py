import numpy as np
from scipy.integrate import quad

# Define the integrand
def integrand(x):
    return (1 + np.log(x)) * np.sqrt(1 + (x * np.log(x))**2)

# Integration limits
a = 0.2
b = 1

# Compute the definite integral
result, _ = quad(integrand, a, b)

# Print the result
print("Value of the definite integral:", result)
