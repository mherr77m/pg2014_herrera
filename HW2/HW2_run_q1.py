# Michael Herrera
# Homework 2 Run Script for Problem 1
# OCNG 689

import numpy as np
import HW2_mod as hw

# Problem 1
# Pass the function two arrays of x,y points and returns
# the distance between all the points between the two arrays.

array1 = np.array([[1,2],[3,4],[5,6],[7,8]])
array2 = np.array([[1,2],[3,4]])

dist = hw.distance(array1,array2)

print "Problem 1:\n"
print "Points from array1"
for p in array1: print '      (%.0f,%.0f)' % (p[0],p[1])
print "Points from array2"
for p in array2: print '      (%.0f,%.0f)' % (p[0],p[1])

print "\nPoint 1   Point 2   Distance"

ic = 0
for i in array1:
    jc = 0
    for j in array2:
        print " (%.0f,%.0f)     (%.0f,%.0f)      %.2f" % \
                (i[0],i[1],j[0],j[1],dist[ic,jc])
        jc += 1
    ic += 1



