# !env python
# Michael Herrera
# 10/18/14
# HW2, Problem 2
# Add a rotate method to the Point class. The rotate
# method must have the ability to rotate around the 
# origin or another point.

import numpy as np

class Point(object):
    """
    Defines a Point object as a point in space.
    Attributes:
        x - x coordinate
        y - y coordinate
    Methods:
        distance - Calculates the distance between two
                   points.
        rotate - Rotates the point by a specified number
                 of radians around another point.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self,other):
        return Point(self.x-other.x, self.y-other.y)

    def __str__(self):
        return '(%.2f, %.2f)' % (self.x, self.y)

    def __repr__(self):
        return 'Point(%.2f, %.2f)' % (self.x, self.y)

    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)

        return np.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

    def rotate(self, angle, p=None):
        if p is None:
            p = Point(0.0, 0.0)

        p_temp = self - p
        self.x = p.x + p_temp.x * np.cos(-angle) - \
                 p_temp.y * np.sin(-angle)
        self.y = p.y + p_temp.x * np.sin(-angle) + \
                 p_temp.y * np.cos(-angle)

if __name__ == '__main__':

    print "Problem 2:\n"

    p1 = Point(2,1)
    print "Point 1:", p1

    angle = 270 * np.pi / 180

    p1.rotate(angle)

    print "Point 1 rotated 270 degrees around the origin:",p1

    p2 = Point(4,5)
    p3 = Point(3,2)
    print "\nPoint 2:", p2
    print "Point 3:", p3

    p2.rotate(angle,p3)

    print "Point 2 rotated 270 degrees around Point 3:",p2




