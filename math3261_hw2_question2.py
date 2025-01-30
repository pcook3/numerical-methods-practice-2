#Parabolic Interpolation function for finding new point
def p_i(f, x1, x2, x3):
    x4 = x2 - (1/2)*((((x2-x1)**2)*(f(x2) - f(x3))) - ((x2-x3)**2)*(f(x2) - f(x1)))/(((x2-x1)*(f(x2) - f(x3))) - (x2-x3)*(f(x2) - f(x1)))
    return x4

#Function f(x)
def f(x):
    return (4*x) - (1.8 * x**2) + (1.2 * x**3) - (0.3 * x**4)

#Parabolic Interpolation function iterating a maximum of 10 times to find a value close to vertex
def para_inter(f, x1 = 1.75, x2 = 2, x3 = 2.5, maxit = 10):
    for i in range(maxit):
        x4 = p_i(f, x1, x2, x3)

        if (x4 < x3) and (x4 > x2):
            if f(x4) < f(x2):
                x1 = x2
                x2 = x4
            else:
                x3 = x4
        else:
            if f(x4) < f(x2):
                x3 = x2
                x2 = x4
            else:
                x1 = x4
    return x4

#Dsiplaying results
print("Estimated Max of : ", f(para_inter(f)), " \nAt: ", para_inter(f))