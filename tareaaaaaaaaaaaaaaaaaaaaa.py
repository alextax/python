# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 22:06:03 2021

@author: alex-PC
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import plot_implicit, symbols, Eq, And
x, y = symbols('x y')
def diferencial(p,w,t):
    a = np.dot(p.T, w) 
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
print(" W: ",dw)
t=0
e=0

dw,e = diferencial(p1,w,t)
print("Diferencial: ",dw)#Diferencial de pesos gradiante
print("Erorr: ",e,"\n")#Error

print("Patron 2")
p2 = np.array([0,-1,1])
print(" W: ",dw)
t =1
dw,e = diferencial(p2,dw,t)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 3")
p3 = np.array([-2,1,0])
print(" W: ",dw)
t=0
dw,e = diferencial(p2,dw,t)
print("Diferencial: ",dw)
print("Error: ",e,"\n")#Error

print("Patron 4")
p4 = np.array([0,2,0])
print(" W: ",dw)
t=0
dw ,e= diferencial(p2,w,t)
print("Diferencial: ",dw)
print("Error: ",e)#Error

p=plot_implicit(dw[0]+ dw[1]*x+dw[2]*y >=0)










