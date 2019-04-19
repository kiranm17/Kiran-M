# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 02:13:13 2019

@author: CSC
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

xyz=np.array(np.random.random((100,3)))
x=xyz[:,0]
y=xyz[:,1]
z=xyz[:,2]*100
fig = plt.figure()