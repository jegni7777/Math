#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 01:51:33 2020

@author: jaegeunkim
"""
"""
This code was written for solving a exercise problem about Theory of Error-correcting Codes during semester course.
We'll define a distance on linear space and find a code with the given minimum distance for any two vectors on that space.
"""

import numpy as np

def add(a): #Binary Operation method which returns a+1 where a is the array.
        if a[0]==0: 
            a[0] = 1
            return a
        elif a[1]==0:
            a[0] = 0
            a[1] = 1
            return a
        elif a[2]==0:
            a[0] = 0
            a[1] = 0
            a[2] = 1
            return a
        elif a[3]==0:
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 1
            return a
        elif a[4]==0:
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 0
            a[4] = 1
            return a
        elif a[5]==0:
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 0
            a[4] = 0
            a[5] = 1
            return a
        elif a[6]==0:
            a[0] = 0
            a[1] = 0
            a[2] = 0
            a[3] = 0
            a[4] = 0
            a[5] = 0
            a[6] = 1
            return a
        else: return "The vector is 111111  "

def addn(a,n): #Binary Operation method with number of add
    for i in range(n):
        add(a)
    return a

def d(a,b):  #Distance method between array and array
    n = 0
    for i in range(7):
        if a[i] != b[i]: n += 1
    return n


def d2(S,b): #Distance method between set and array
    min = 7
    for a in S:
        if d(a,b) < min : min = d(a,b)
    return min

zero = np.array([0,0,0,0,0,0,0])
one = np.array([1,1,1,1,1,1,1])
u = np.array([0,0,0,0,0,0,0])
S = []

for i in range(128):
    S = []
    u = zero.copy()
    addn(u,i)
    S.append(u.copy())
    for j in range(128-i):
        if u.all() : break
        add(u)
        if d2(S,u) >= 4: S.append(u.copy())
    print("The length is",len(S))
    print(S)
    print()