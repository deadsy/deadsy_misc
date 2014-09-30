#! /usr/bin/python

#------------------------------------------------------------------------------
"""

Intersect two cylinders
Create a 2D surface that can be wrapped around the cylinder to show the intersection curve.
That is: Create printable paper cutting templates for pipe intersection.

"""
#------------------------------------------------------------------------------

import math
from dxfwrite import DXFEngine as dxf

#------------------------------------------------------------------------------

# number of divisions around the cylinder circumference
_NDIVS = 32

#------------------------------------------------------------------------------

def dot(u, v):
    return (u[0] * v[0]) + (u[1] * v[1]) + (u[2] * v[2])

def scale(v, k):
    return (v[0] * k, v[1] * k, v[2] * k)

def normalize(v):
    l = math.sqrt(dot(v, v))
    return scale(v, 1.0/l)

def cross(u, v):
    return ((u[1] * v[2]) - (u[2] * v[1]), (u[2] * v[0]) - (u[0] * v[2]), (u[0] * v[1]) - (u[1] * v[0]))

#------------------------------------------------------------------------------

def gen_normal(v):
    """return a normal to the vector"""
    if v[0] == 0.0:
        return (1.0, 0.0, 0.0)
    if v[1] == 0.0:
        return (0.0, 1.0, 0.0)
    if v[2] == 0.0:
        return (0.0, 0.0, 1.0)
    return (0.0, v[2], -v[1])

#------------------------------------------------------------------------------

def quadratic(a, b, c):
    """return real solutions for a qaudratic"""
    a = float(a)
    b = float(b)
    c = float(c)
    if a == 0.0:
        if b == 0.0 and c == 0.0:
            return ('inf',)
        if b == 0.0 and c != 0.0:
            return ('inv',)
        if b != 0.0 and c == 0.0:
            return ('1', 0.0)
        if b != 0.0 and c != 0.0:
            return ('1', -c / b)
    # use the general form solution
    d = (b * b) - 4.0 * a * c
    if d == 0.0:
        return ('1', -b / (2.0 * a))
    if d < 0.0:
        # no real solutions
        return ('0',)
    d = math.sqrt(d)
    return ('2', (-b + d)/(2.0 * a), (-b - d)/(2.0 * a))

#------------------------------------------------------------------------------

class cylinder:
    def __init__(self, o, a, r, l):
        """
        o = origin coordinates
        a = axis vector
        l = length
        r = radius
        """
        self.o = o
        self.a = normalize(a)
        self.r = r
        self.l = l

    def gen_lines(self):
        """
        Generate the cylinder surface lines used to intersect with
        the other cylinder.
        """
        # 1st normal to cylinder axis
        u = normalize(gen_normal(self.a))
        # 2nd normal to cylinder axis
        v = normalize(cross(self.a, u))
        lines = []
        # step around the parameterised base circle
        for i in range(_NDIVS):
            theta = 2.0 * math.pi * i / _NDIVS
            rc = self.r * math.cos(theta)
            rs = self.r * math.sin(theta)
            l = (self.o[0] + (rc * u[0]) + (rs * v[0]),
                 self.o[1] + (rc * u[1]) + (rs * v[1]),
                 self.o[2] + (rc * u[2]) + (rs * v[2]))
            # the line starts at point l and is in the direction of the cylinder axis
            lines.append((l, self.a))
        return lines

    def __str__(self):
        s = []
        s.append('o = (%f,%f,%f)' % (self.o[0], self.o[1], self.o[2]))
        s.append('a = (%f,%f,%f)' % (self.a[0], self.a[1], self.a[2]))
        s.append('r = %f' % self.r)
        s.append('l = %f' % self.l)
        return ' '.join(s)

    def intersect_line(self, l):
        """
        Intersect a line with this cylinder.
        """
        # x = a + tn
        pass


#------------------------------------------------------------------------------

def main():

    c0 = cylinder((0,0,0), (0,0,1), 1, 10)
    print c0
    lines = c0.gen_lines()

    drawing = dxf.drawing('test.dxf')

    pl = dxf.polyline()
    for l in lines:
        pl.add_vertex(l[0])
    pl.close()
    drawing.add(pl)
    drawing.save()

    print quadratic(0,0,0)
    print quadratic(0,0,1)
    print quadratic(0,1,0)
    print quadratic(0,1,1)
    print quadratic(1,0,0)
    print quadratic(1,0,1)
    print quadratic(1,1,0)
    print quadratic(1,1,1)

    print quadratic(1,2,3)
    print quadratic(3,2,1)
    print quadratic(1,-4,3)
    print quadratic(1,-1,-2)
    print quadratic(1,0,-25)



main()

#------------------------------------------------------------------------------

