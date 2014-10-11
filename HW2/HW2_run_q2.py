# Michael Herrera
# Homework 2 Run Script for Problem 2
# OCNG 689

import numpy as np
import HW2_mod as hw

# Problem 2
# Add a rotate method to the Point class. The rotate
# method must have the ability to rotate around the 
# origin or another point.

print "Problem 2:\n"

p1 = hw.Point(2,1)
print "Point 1:", p1

angle = 270 * np.pi / 180

p1.rotate(angle)

print "Point 1 rotated 270 degrees around the origin:",p1

p2 = hw.Point(4,5)
p3 = hw.Point(3,2)
print "\nPoint 2:", p2
print "Point 3:", p3

p2.rotate(angle,p3)

print "Point 2 rotated 270 degrees around Point 3:",p2




