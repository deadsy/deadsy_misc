#! /usr/bin/python

#------------------------------------------------------------------------------
"""

Intersect two cylinders
Create a 2D surface that can be wrapped around the cylinder to show the intersection curve.
That is: Create printable paper cutting templates for pipe intersection.

"""
#------------------------------------------------------------------------------

import math

#------------------------------------------------------------------------------

# number of divisions around the cylinder circumfrence
_NDIVS = 32

#------------------------------------------------------------------------------

def normalize(x):
    l = math.sqrt((x[0]*x[0]) + (x[1]*x[1]) + (x[2]*x[2]))
    return (x[0]/l, x[1]/l, x[2]/l)

#------------------------------------------------------------------------------

class cylinder:
    def __init__(self, x, v, r, l):
        """
        x = origin coordinates
        v = direction vector
        l = length
        r = radius
        """
        self.x = x
        self.v = normalize(v)
        self.r = r
        self.l = l

    def __str__(self):
        s = []
        s.append('x = (%f,%f,%f)' % (self.x[0], self.x[1], self.x[2]))
        s.append('v = (%f,%f,%f)' % (self.v[0], self.v[1], self.v[2]))
        s.append('r = %f' % self.r)
        s.append('l = %f' % self.l)
        return ' '.join(s)

#------------------------------------------------------------------------------

def main():

    c0 = cylinder((0,0,0), (1,0,0), 2, 10)
    print c0

main()

#------------------------------------------------------------------------------

