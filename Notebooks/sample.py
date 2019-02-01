# -*- coding: utf-8 -*-
"""
--------1D Lagrange interpolation problem---------------
"""
#
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
#from sympy import *
from sympy import init_printing
init_printing()
#
fx  = lambda x: x**3+4.0*x**2-10.0

npts = 200 
xx = np.linspace(-1, 1, npts)
yy = np.zeros((npts))
zz = np.zeros((npts))


yy[:] = fx(xx[:])
plt.figure(0)
plt.plot(xx, yy ,'r--')
#
x= sp.symbols('x')
N = x**3+4.0*x**2-10.0
fdx = sp.diff(N , x)

for i in range(npts):
    zz[i] =  fdx.subs([(x, xx[i])])

plt.figure(1)
plt.plot(xx, zz ,'r--')   