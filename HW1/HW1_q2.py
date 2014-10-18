# !env python
# Michael Herrera
# 10/17/14
# HW1, Problem 2
#
# Write a function to compute the integral of a list of numbers
# [f_n(x_n)] using the trapezoidal rule with a default value of dx=1.0

def integrate(f,dx=1.0):
    """
    Computes the integral of a list of numbers using the trapezoidal rule
    Inputs
        f  = List of values in function
        dx = Grid spacing, default of 1.0
    Output
        var =  Integral of function
    """
    if (len(f) >2 ):
        var = (dx/2.0)*(f[0]+2*sum(f[1:-1])+f[-1])
    else:
        var = (dx/2.0)*(sum(f))
    return var

if __name__ == '__main__':
    f = [1.0, 3.0, 4.0, 5.0]
    print 'Problem 2:'
    print 'f = ',f
    print 'integrate(f): ',integrate(f)
    print 'integrate(f,dx=0.5): ',integrate(f,dx=0.5)






