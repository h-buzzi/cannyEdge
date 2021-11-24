# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 08:21:06 2021

@author: hbuzzi
"""

import cv2
import numpy as np
import time

def imshow_close_withAny(image,text = " "): #Função que mostra a imagem e permite fechá-la com qualquer tecla
    """Função que mostra uma imagem e permite que seja fechada quando qualquer tecla for pressionada.
    
    Input: Imagem a ser mostrada, Título da imagem.
    
    Output: None"""
    cv2.imshow(text, image) #Mostra imagem
    key = cv2.waitKey(0) #Espera tecla
    if key != None:  #Se tiver alguma tecla
        cv2.destroyWindow(text) #Fecha a imagem
        return
    
def canny_Edge(I, d_padrao, l_Sup, l_Inf):
    def possible_Edges(comp, step, eix):
        ind1 = np.roll(comp, step, axis = eix)
        ind2 = np.roll(comp, -step, axis = eix)
        ind3 = (M*comp > M*ind1) == (M*comp > M*ind2)
        gN[ind3] = M[ind3]
        return
        
    I = np.float32(I)
    k = 6*d_padrao+1
    I = cv2.GaussianBlur(I,(k,k),d_padrao)
    
    K_c = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    K_l = K_c.T
    I_c = cv2.filter2D(src = I, ddepth = -1, kernel = K_c)
    I_l = cv2.filter2D(src = I, ddepth = -1, kernel = K_l)
    
    M = np.sqrt((I_c*I_c) + (I_l*I_l))
    P = np.arctan2(I_c,I_l)*180/np.pi
    P[P<0]=P[P<0]+180
    gN = np.zeros(I.shape)
    
    for i in range(4):
        if i==0:
            possible_Edges((P<22.5) + (P>=157.5), 1, 1)
        elif i==1:
            possible_Edges((P>=22.5)*(P<67.5), 1, (0,1))
        elif i==2:
            possible_Edges((P>=67.5)*(P<112.5), 1, 0)
        elif i==3:
            ind1 = (P>=112.5)*(P<157.5)
            ind2 = np.roll(ind1,(1,-1),axis=(1,0))
            ind3 = np.roll(ind1,(1,-1),axis=(0,1))
            ind4 = (M*ind1 > M*ind2) == (M*ind1 > M*ind3)
            gN[ind4] = M[ind4]
    ##Imagens binárias
    gNH = 255*np.ones(I.shape,dtype=np.uint8)*(gN>(l_Sup*np.amax(gN)))
    gNL = 255*np.ones(I.shape,dtype=np.uint8)*(gN>l_Inf*np.amax(gN))
    return gNH, gNL
###### INPUTS
start = time.time()
I = cv2.imread('castle.jpg', cv2.IMREAD_GRAYSCALE)
dp = 2 # Sigma
l_Sup = 0.45
l_Inf = 0.1

### Função
gNH, gNL = canny_Edge(I, dp, l_Sup, l_Inf)
imshow_close_withAny(gNH, 'gNH')
imshow_close_withAny(gNL,'gNL')