import numpy as np
import sys
import math

#Bisection Method
def bisect1(func,xl,xu):
    smallenough = False
    if func(xl)*func(xu)>0:
        sys.exit('initial estimates do not bracket solution, re-run program\n')
    while not smallenough:
        xm = (xl+xu)/2
        if func(xm)*func(xl)>0:
            if relative_error(xl, xm):
                smallenough = True
                break
            xl = xm
        else:
            if relative_error(xu, xm):
                smallenough = True
                break
            xu = xm
    return xm

#Function for equation
def A(x):
    e = math.e
    root = 5 - (5*x) - (e ** (x/2))
    return root

#Boolean function for r.e. less than 1%
def relative_error(old_x, new_x):
    if np.absolute((new_x - old_x)/(new_x)) < .01:
        return True
    else:
        return False

#Gathering input for brackets
xl = int(input("\nLower Bound: "))
xu = int(input("Upper Bound: "))
answer = round(bisect1(A, xl, xu), 6)

#Displaying results
print(answer)

