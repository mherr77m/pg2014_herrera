import HW1_mod as hw

# Michael Herrera
# OCNG 689
# Homework 1

# I have written the functions for homework 1 in a 
# single module that is imported in this run script.

print 'Michael Herrera'
print 'OCNG 689'
print 'Homework 1\n'

# 1.  Write a function to return a list of N Fibonacci numbers.
print 'Problem 1:'
print 'fib(1): ',hw.fib(1)
print 'fib(2): ',hw.fib(2)
print 'fib(6): ',hw.fib(6)

# 2.  Write a function to compute the integral of a list of numbers 
#     [f_n(x_n)] using the trapezoidal rule with a default value of dx=1.0

f = [1.0, 3.0, 4.0, 5.0]
print '\nProblem 2:'
print 'integrate(f): ',hw.integrate(f)
print 'integrate(f,dx=0.5): ',hw.integrate(f,dx=0.5)

# 3.  Write a function to read the data from the file discharge.dat, 
#    return a list of dates (as datetime objects) and discharge (ignoring any flags).

filename = '/Users/Michael/Documents/ocng689/pg2014/HW1/discharge.dat'
date,discharge = hw.read_dat(filename)

print '\nProblem 3:'
print '   Date      Discharge(ft^3/s)'
for i in range(0,10):
	print date[i],'       ',discharge[i]

# 4. Write a function to read data from the file drifter.dat.  Return a dictionary based on the track name as indices, returning a list of lat/lon pairs:

filename = '/Users/Michael/Documents/ocng689/pg2014/HW1/drifter.dat'
tracks = hw.read_drifter(filename)

print '\nProblem 4:'
print 'tracks[''FRODO''] :',tracks['FRODO']
print 'tracks[''STRIDER''] :',tracks['STRIDER']
