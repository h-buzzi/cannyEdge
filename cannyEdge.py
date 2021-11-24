# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:21:06 2021

@author: hbuzzi
"""

import cv2
import numpy as np
import time

###### INPUTS
start = time.time()
I = np.float32(cv2.imread('castle.jpg', cv2.IMREAD_GRAYSCALE))
dp = 2 # Sigma
l_Sup = 0.45
l_Inf = 0.1

###### Suaviza imagem por GaussianBlur
k = 6*dp+1
Is = cv2.GaussianBlur(I,(k,k),dp)

###### Magnitude e fase
K_c = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
K_l = K_c.T
I_c = cv2.filter2D(src = Is, ddepth = -1, kernel = K_c)
I_l = cv2.filter2D(src = Is, ddepth = -1, kernel = K_l)

M = np.sqrt((I_c*I_c) + (I_l*I_l))
P = np.arctan2(I_c,I_l)*180/np.pi
P[P<0]=P[P<0]+180
G_N = np.zeros(I.shape)

## 1
ind1 = (P<22.5) + (P>=157.5) 
ind2 = np.roll(ind1,-1,axis=1)
ind3 = np.roll(ind1,1,axis=1)
ind4 = (M*ind1 > M*ind2) == (M*ind1 > M*ind2)
G_N[ind4] = M[ind4]

## 2
ind1 = (P>=22.5)*(P<67.5)
ind2 = np.roll(ind1,-1,axis=(0,1))
ind3 = np.roll(ind1,1,axis=(0,1))
ind4 = (M*ind1 > M*ind2) == (M*ind1 > M*ind3)
G_N[ind4] = M[ind4]

## 3
ind1 = (P>=67.5)*(P<112.5)
ind2 = np.roll(ind1,-1,axis=0)
ind3 = np.roll(ind1,1,axis=0)
ind4 = (M*ind1 > M*ind2) == (M*ind1 > M*ind2)
G_N[ind4] = M[ind4]

## 4
ind1 = (P>=112.5)*(P<157.5)
ind2 = np.roll(ind1,(1,-1),axis=(1,0))
ind3 = np.roll(ind1,(1,-1),axis=(0,1))
ind4 = (M*ind1 > M*ind2) == (M*ind1 > M*ind2)
G_N[ind4] = M[ind4]

##Imagens binárias
G_NH = 255*np.ones(I.shape,dtype=np.uint8)*(G_N>(l_Sup*np.amax(G_N)))
G_NL = 255*np.ones(I.shape,dtype=np.uint8)*(G_N>l_Inf*np.amax(G_N))
print(time.time()-start)
cv2.imwrite('D:\Trabalho\Python\cannyEdge-main\saida.jpg',G_NH)
cv2.imshow('G_NH', G_NH)
cv2.waitKey(0)
cv2.imshow('G_NL', G_NL)
cv2.waitKey(0)
