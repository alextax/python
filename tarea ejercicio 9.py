# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 20:43:26 2021

@author: aaaa-PC
"""

import matplotlib.pyplot as plt
import numpy as np

def obtenerDiferencial(p,w,t):
    a = np.dot(p.T, w)  # lo que obtenemos de la neurona
    if a >= 0:
        a = 1
    else:
        a = 0

    e = t - a
    diferenciaW = np.array([])

    for x in range(0,3):
        a = -2*(t-p[x]*w[x])*p[x]
        diferenciaW = np.insert(diferenciaW,x,a)


    return diferenciaW,e

dw = np.array([])
print("Patron 1")
w= np.array([0.5,0.5,0.5]) #peso anterior
          # x1, x2, t
p1 = np.array([3,1,0]) #patron 1
print("Patron: ",p1," Pesos: ",w)
t=0
e=0

dw,e = obtenerDiferencial(p1,w,t)
print("Diferencial: ",dw)#Diferencial de pesos gradiante
print("Erorr: ",e,"\n")#Error

print("Patron 2")
p2 = np.array([0,-1,1])
print("Patron: ",p2," Pesos: ",dw)
t =1
dw,e = obtenerDiferencial(p2,dw,t)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 3")
p3 = np.array([-2,1,0])
print("Patron: ",p3," Pesos: ",dw)
t=0
dw,e = obtenerDiferencial(p2,dw,t)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 4")
p4 = np.array([0,2,0])
print("Patron: ",p4," Pesos: ",dw)
t=0
dw ,e= obtenerDiferencial(p2,w,t)
print("Diferencial: ",dw)
print("Error: ",e)#Error



