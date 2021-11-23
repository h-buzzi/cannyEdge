# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:21:06 2021

@author: hbuzzi
"""

import cv2
import sys
import numpy as np
from matplotlib import pyplot as pp

###### INPUTS
I = cv2.imread('castle.jpg', cv2.IMREAD_GRAYSCALE)
dp = 2 # Sigma
l_Sup = 0.5
l_Inf = 0.1

###### Suaviza imagem por GaussianBlur
k = 6*dp+1
Is = cv2.GaussianBlur(I,(k,k),dp)

###### Magnitude e fase
K_c = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
K_l = K_c.T
I_c = cv2.filter2D(src = Is, ddepth = -1, kernel = K_c)
I_l = cv2.filter2D(src = Is, ddepth = -1, kernel = K_l)

M = np.sqrt(I_c*I_c + I_l*I_l)
cv2.imshow('M', np.uint8(255*M/np.amax(M)))
cv2.waitKey(0)
P = np.arctan2(I_c,I_l)*180/np.pi
P[P<0]=P[P<0]+180
G_N = np.zeros(I.shape)

## 1
ind1 = P<22.5
ind2 = np.roll(ind1,-1,axis=1)
ind3 = np.roll(ind1,1,axis=1)
A = np.zeros(I.shape)
B = A
C = A
A[ind1] = M[ind1]
B[ind2] = M[ind2]
C[ind3] = M[ind3]
ind4 = (A > B) == (A > C)
G_N[ind4] = M[ind4]

## 2
ind1 = (P>=22.5)*(P<67.5)
ind2 = np.roll(ind1,-1,axis=(0,1))
ind3 = np.roll(ind1,1,axis=(0,1))
A = np.zeros(I.shape)
B = A
C = A
A[ind1] = M[ind1]
B[ind2] = M[ind2]
C[ind3] = M[ind3]
ind4 = (A > B) == (A > C)
G_N[ind4] = M[ind4]
## 3

