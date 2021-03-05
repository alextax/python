# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 12:49:20 2021

@author:XD

"""

import numpy as np

#funcion de w 
w = np.array([ 0.5 , 1.3 , -0.8])

#funcion de patrones
patron1 = np.array([1,2,1])
t=1

a = np.dot(patron1,w)
print(a)

if a >= 0:
  a = 1
else:
  a = 0
print(a)

e=t-a
wnuevo=w + e*patron1
print(e)
print(wnuevo)