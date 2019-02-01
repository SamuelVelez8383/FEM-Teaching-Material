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
    Shape functions
    """
    sh=zeros(4)
    N=zeros(2 , 8)
    sh[0] =(1.0/4.0)*(1 - x)*(1 - y)
    sh[1] =(1.0/4.0)*(1 + x)*(1 - y)
    sh[2] =(1.0/4.0)*(1 + x)*(1 + y)
    sh[3] =(1.0/4.0)*(1 - x)*(1 + y)
    for i in range(4):
        j=2*i
        N[0,j]  =sh[i]
        N[1,j+1]=sh[i]
#
    return N


def sfder4(x,y):
    """
    Shape function derivatives
    """
    dhdx = zeros(2,4)
    sh=zeros(4)
    sh[0] =(1.0/4.0)*(1 - x)*(1 - y)
    sh[1] =(1.0/4.0)*(1 + x)*(1 - y)
    sh[2] =(1.0/4.0)*(1 + x)*(1 + y)
    sh[3] =(1.0/4.0)*(1 - x)*(1 + y)   
    for i in range(4):
        dhdx[0,i]=diff(sh[i],x)
        dhdx[1,i]=diff(sh[i],y)
    
    return dhdx


def stdm4(x,y): 
    """
    Strain-dispacement interpolator
    """
    B    = zeros(3,8)
    dhdx = sfder4(x,y)
    for i in range(4):
        B[0,   2*i] = dhdx[0,i]
        B[1, 2*i+1] = dhdx[1,i]
        B[2,   2*i] = dhdx[1,i]
        B[2, 2*i+1] = dhdx[0,i]        

    return B

#Estiramiento en x
#u = Matrix(8, 1, [ -0.2 , 0.0 , 0.2 , 0.0 , 0.2 , 0.0 , -0.2 , 0.0])
#Estiramiento en y
#u = Matrix(8, 1, [ 0.0 , -0.2 , 0.0 , -0.2 , 0.0 , 0.2 , 0.0 , 0.2])
#Cortante
#u = Matrix(8, 1, [-0.2 , 0.0 , -0.2 , 0.0 , 0.2 , 0.0 , 0.2 , 0.0])
#Mixto
u = Matrix(8, 1, [-0.2 ,-0.2 , 0.2 , -0.2 , -0.2 , 0.2 , 0.2 , 0.2])
x , y = symbols('x y') 
h=symbols('h')
#
# Simbolically compute matrices
#
N = sha4(x,y)
B = stdm4(x,y)
#
li=-1.0
ls= 1.1
dl= 0.1
npts=int((ls-li)/dl)
USOL = np.zeros((npts, npts, 2))
ESOL = np.zeros((npts, npts, 3))
xx, yy = np.mgrid[li:ls:npts*1j, li:ls:npts*1j]
#
for i in range(npts):
    for j in range(npts):
        NS =N.subs([(x, xx[i,j]), (y, yy[i,j]), (h, 1.00)])
        BS =B.subs([(x, xx[i,j]), (y, yy[i,j]), (h, 1.00)])
        up  = NS*u
        eps = BS*u
        USOL[i, j, 0] = up[0]
        USOL[i, j, 1] = up[1]
        ESOL[i, j, 0] = eps[0]
        ESOL[i, j, 1] = eps[1]
        ESOL[i, j, 2] = eps[2]

plt.figure(1)
plt.contourf(xx , yy , USOL[:,:,0], cmap="RdYlBu")
plt.figure(2)
plt.contourf(xx , yy , USOL[:,:,1], cmap="RdYlBu")
plt.figure(3)
plt.contourf(xx , yy , ESOL[:,:,0], cmap="RdYlBu")
plt.figure(4)
plt.contourf(xx , yy , ESOL[:,:,1], cmap="RdYlBu")
plt.figure(5)
plt.contourf(xx , yy , ESOL[:,:,2], cmap="RdYlBu")





















