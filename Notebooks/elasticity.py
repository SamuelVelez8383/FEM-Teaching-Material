# -*- coding: utf-8 -*-
"""
Elasticity solutions calculator
Juan Gomez
Nicolas Guarin
"""
from __future__ import division, print_function
import scipy.special as sci
import numpy as np
from numpy import sin, cos, sqrt, pi


def myfunction(x, y, p):
    """
    Template for user defined elasticity solution.
    """
    ux=(x**2.+y**2.)**p
#    ux= -x-y
    return ux

