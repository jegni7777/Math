#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:58:15 2020

@author: jaegeunkim
"""
"""
This code was written to make graphs of a function that is noncontinuously differentiable.
"""


from math import *
import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-1e-10, 0, 1e-11)
y1 = (x1**2)*np.sin(1/x1)
plt.plot(x1,y1,'x-')
plt.grid(True)

x2 = np.arange(0, 1e-10, 1e-11)
y2 = (x2**2)*np.sin(1/x2)
plt.plot(x2,y2,'x-')
plt.grid(True)
plt.plot(0,0,'x')
plt.savefig('noncontinuously differentiable function0',format='png')