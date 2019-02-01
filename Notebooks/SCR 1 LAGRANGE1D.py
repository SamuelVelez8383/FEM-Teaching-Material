# -*- coding: utf-8 -*-
"""
--------1D Lagrange interpolation problem---------------
"""
#
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
#from sympy import *
#from sympy import init_printing
#init_printing()
#
def LagrangPoly(x,order,i,xi=None):
    if xi==None:
        xi=sym.symbols('x:%d'%(order+1))
    index = range(order+1)
    index.pop(i)
    return sym.prod([(x-xi[j])/(xi[i]-xi[j]) for j in index])
#
fx  = lambda x: x**3+4.0*x**2-10.0
fdx = lambda x: 3*x**2+8.0*x 
#
# Assign symbols
#
x= sym.symbols('x')
#
# Create arrays
#
npts = 200
xx = np.linspace(-1, 1, npts)
yy = np.zeros((npts))
yd = np.zeros((npts)) 
zz = np.zeros((npts))
fd = np.array([fx(-1.0), fx(1.0) ,fx(0.0), fx(-0.5), fx(0.5)])
fc = np.array([fdx(-1.0), fdx(1.0) ,fdx(0.0), fdx(-0.5), fdx(0.5)])
#
#
# Derive Lagrange polynomials.
#
pol = []
pol.append(sym.simplify(LagrangPoly(x, 4, 0, [-1,1,0,-0.5, 0.5])))
pol.append(sym.simplify(LagrangPoly(x, 4, 1, [-1,1,0,-0.5, 0.5])))
pol.append(sym.simplify(LagrangPoly(x, 4, 2, [-1,1,0,-0.5, 0.5])))
pol.append(sym.simplify(LagrangPoly(x, 4, 3, [-1,1,0,-0.5, 0.5])))
pol.append(sym.simplify(LagrangPoly(x, 4, 4, [-1,1,0,-0.5, 0.5])))
#
#  Print each polynom.
#
print "First   polynomial", pol[0]
print "Second  polynomial", pol[1]
print "Third   polynomial", pol[2]
print "Fourth  polynomial", pol[3]
print "Fifth   polynomial", pol[4]
#
# Print and plot the complete polynom.
#
print
print pol[0]*fd[0]+pol[1]*fd[1]+pol[2]*fd[2]+pol[3]*fd[3]+pol[4]*fd[4]
print
##
plt.figure()
for k in range(5):
    for i in range(npts):
        yy[i] =  pol[k].subs([(x, xx[i])])
    plt.plot(xx, yy)
plt.axhline(y=1)
plt.grid()
#
# Plot the resultant polyn., the actual function and the known points.
#
plt.figure()
for i in range(npts):
    yy[i] = fd[0]*pol[0].subs([(x, xx[i])]) + fd[1]*pol[1].subs([(x, xx[i])]) \
          + fd[2]*pol[2].subs([(x, xx[i])]) + fd[3]*pol[3].subs([(x, xx[i])]) \
          + fd[4]*pol[4].subs([(x, xx[i])])
plt.plot(xx, yy)
for i in range(npts):
    zz[i]=fx(xx[i])
plt.plot(xx, zz,'r--')
plt.plot([-1, 1, 0, -0.5, 0.5], fd, 'ko')
#
# Compute first order derivatives
#
dpol = []
dpol.append(sym.diff(pol[0],x))
dpol.append(sym.diff(pol[1],x))
dpol.append(sym.diff(pol[2],x))
dpol.append(sym.diff(pol[3],x))
dpol.append(sym.diff(pol[4],x))
print "First   derivative"  , dpol[0]
print "Second  derivative"  , dpol[1]
print "Third   derivativel" , dpol[2]
print "Fourth  derivative"  , dpol[3]
print "Fifth   derivativel" , dpol[4]
#
# Print and plot the complete resultant derivative
#
print dpol[0]*fd[0]+dpol[1]*fd[1]+dpol[2]*fd[2]+dpol[3]*fd[3]+dpol[4]*fd[4]
print
#
plt.figure()
for k in range(5):
    for i in range(npts):
        yd[i] = dpol[k].subs([(x, xx[i])])
    plt.plot(xx, yd)
#    plt.savefig('deriv2.pdf')
#
#
# Plot the complete derivative, the actual derivative and the known points.
#
plt.figure()
for i in range(npts):
    yd[i] = fd[0]*dpol[0].subs([(x, xx[i])]) + fd[1]*dpol[1].subs([(x, xx[i])]) \
          + fd[2]*dpol[2].subs([(x, xx[i])]) + fd[3]*dpol[3].subs([(x, xx[i])]) \
          + fd[4]*dpol[4].subs([(x, xx[i])])
plt.plot(xx, yd)
#
for i in range(npts):
    zz[i]=fdx(xx[i])
plt.plot(xx, zz)
plt.plot([-1, 1, 0, -0.5, 0.5], fc, 'ko')
#plt.savefig('firstder.pdf')







































   