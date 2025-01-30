import numpy as np
import math

def f(x):
    e = math.e
    return (e**(-x))**2

def second_derivative_f(x):
    e = math.e
    return (4 * (x**2) * ((e**(-x))**2)) - (2 * ((e**(-x))**2))  # Second derivative of f(x)

def golden_section_search(func, a, b, tol=1e-5):
    phi = (1 + np.sqrt(5)) / 2  # Golden Ratio
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while abs(b - a) > tol:
        if func(x1) < func(x2):
            b = x2
        else:
            a = x1

        x1 = b - (b - a) / phi
        x2 = a + (b - a) / phi

    return (a + b) / 2  # Approximate inflection point

# Finding the inflection point
inflection_x = golden_section_search(lambda x: abs(second_derivative_f(x)), a=0, b=2)
print(f"Approximate inflection point: x = {inflection_x:.5f}")
