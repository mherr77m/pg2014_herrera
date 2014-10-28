# !env python
# Michael Herrera
# 10/18/14
# HW2, Problem 1
# Pass the function two arrays of x,y points and returns
# the distance between all the points between the two arrays.

import numpy as np

def distance(array1,array2):
    """
    Calculates the distance between all points in two
    arrays.  The arrays don't have to be the same size.
    Each array has the form [[x1,y1],[x2,y2],...,[xn,yn]]
    """

    # Use array broadcasting in the distance formula to
    # allow for arrays of different sizes
    dist = np.sqrt((array1[:,0,np.newaxis] - array2[:,0])**2 + \
                   (array1[:,1,np.newaxis] - array2[:,1])**2)
    return dist

if __name__ == '__main__':

    array1 = np.array([[1,2],[3,4],[5,6],[7,8]])
    array2 = np.array([[1,2],[3,4]])

    dist = distance(array1,array2)

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



