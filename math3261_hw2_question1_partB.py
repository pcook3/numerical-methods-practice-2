import numpy as np
import math

#Newton's Method
def newtraph(f,fp,x0,Ea,maxit=30):
    for i in range(maxit):
        x1 = x0 - f(x0)/fp(x0)
        ea = np.absolute((x1-x0)/x1)
        if ea < Ea:  break
        x0 = x1
    return x1,f(x1),ea,i+1

#Function
def f(x):
    e = math.e
    root = 5 - (5*x) - (e ** (x/2))
    return root

#First derivative of function
def fp(x):
    e = math.e
    root = -5 - (1/2)*(e**(x/2))
    return root

#Displaying results
x0 = 0.7
(xsoln,fxsoln,ea,n) = newtraph(f,fp,x0,Ea=.01)
print('Solution = {0:8.5g}'.format(xsoln))
print('Function value at solution = {0:8.5e}'.format(fxsoln))
print('Relative error = {0:8.3e}'.format(ea))
print('Number of iterations = {0:5d}'.format(n))