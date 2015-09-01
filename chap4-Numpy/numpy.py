# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:54:37 2015

@author: chris
"""

import numpy as np

data1=[6,7.5,8,0,1]
arr1=np.array(data1,dtype=np.float64)
print arr1.dtype
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
print arr2
print arr2.ndim
print arr2.shape
print arr1.dtype

print np.zeros(10)
print np.zeros((3,6))

print np.empty((2,3,2))
bouya=np.arange(0,15)
print bouya.dtype
myFloatArr=bouya.astype(np.float)
print myFloatArr.dtype

arr=np.array([[1.,2.,3.],[4.,5.,6.]])
print arr
print arr*arr
print arr-arr
print 1/arr
print arr**0.5

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print arr2d[2][1]
print arr2d[2,1]

#Random walk example
import random
from matplotlib import pylab as plt
position=0
walk=[position]
steps=100
for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position +=step
    walk.append(position)

plt.plot([x for x in range(steps+1)],walk)