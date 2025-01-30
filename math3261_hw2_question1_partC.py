import math
import numpy as np

#Secant Method
def secant_method(f, x0, x1):
    smallenough = False

    while not smallenough:
 
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            raise ValueError("Division by zero encountered in secant method")
        
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if relative_error(x1, x_new):
            smallenough = True
            return x_new
        
        x0, x1 = x1, x_new
    
    raise ValueError("Secant method did not converge within the maximum number of iterations")

#Function:
def func(x):
    e = math.e
    root = 5 - (5*x) - (e ** (x/2))
    return root

#returning whether or not r.e. is less than 1%
def relative_error(old_x, new_x):
    if np.absolute((new_x - old_x)/(new_x)) < .01:
        return True
    else:
        return False

root = secant_method(func, 0.0, 2.0)
print("Root:", root)