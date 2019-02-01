#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:56:35 2017
Displacement and strain interpolation
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from sympy import *


def sha4(x,y):
    """
    Compute the shape functions for bi-linear
    square element of size 2.0.
    """
    sh=zeros(4)
    N=zeros(2 , 8)
    sh[0] =(1.0/4.0)*(1 - x)*(1 - y)
    sh[1] =(1.0/4.0)*(1 + x)*(1 - y)
    sh[2] =(1.0/4.0)*(1 + x)*(1 + y)
    sh[3] =(1.0/4.0)*(1 - x)*(1 + y)
#
    return sh

u = Matrix(4, 1, [-0.2 ,0.2 ,-0.2 , 0.2])
x , y = symbols('x y') 
#
# Simbolically compute matrices
#
H = sha4(x,y)
#
li=-1.0
ls= 1.1
dl= 0.1
npts=int((ls-li)/dl)
USOL = np.zeros((npts, npts, 1))
xx, yy = np.mgrid[li:ls:npts*1j, li:ls:npts*1j]
#
for i in range(npts):
    for j in range(npts):
        NS =H.subs([(x, xx[i,j]), (y, yy[i,j])])
        up  = NS*u
        USOL[i, j, 0] = up[0]

plt.figure(1)
plt.contourf(xx , yy , USOL[:,:,0], cmap="RdYlBu")
#plt.figure(2)
#plt.contourf(xx , yy , USOL[:,:,1], cmap="RdYlBu")
#plt.figure(3)
#plt.contourf(xx , yy , ESOL[:,:,0], cmap="RdYlBu")
#plt.figure(4)
#plt.contourf(xx , yy , ESOL[:,:,1], cmap="RdYlBu")
#plt.figure(5)
#plt.contourf(xx , yy , ESOL[:,:,2], cmap="RdYlBu")





















