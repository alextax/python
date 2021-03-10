# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:24:29 2021

@author: Alex-PC
"""

#Para empezar necesitamos importar numpy para operaciones

# También necesitamos pyplot que contiene el método SCARTTER  para hacer la grafica de dispersión 

import numpy as np 

import matplotlib.pyplot as plt

#Para usar el metodo scatter  perteneciente a pyplot necesitamos dos pares ordenados de datos                          

#podemos ver que uso dos arrays con la misma cantidad de datos. x con 14 datos y y con 14 

x = np.array([23,18,30,24,29,45,10,17,27,39,32,40,21,14])

y = np.array([62,72,54,60,57,30,79,65,55,34,48,41,68,76])

#solo llamamos al metodo y usamos los datos que los graficara asi (23,62)        

#y asi sucesivamente por eso es necesario tener la misma cantidad de datos 

plt.scatter(x, y)

#desplegamos

plt.show()


#Ejemplo 2  con dos graficas al mismo tiempo 

#declaramos el vector 

x=[1,2,3,4,5] 

#obtenemos los valores de y1 y y2

y1=[i**2 for i in x]

y2=[2*i+1 for i in x]

#ploteamos los respectivos datos y para difenciar cambiamos de color y forma

plt.title("2 graficas de dispersion ")
plt.scatter(x,y1,marker="x",color='r',label="x**2")

plt.scatter(x,y2,marker="o",color='b',label="2*x+1")

#deplegamos la leyenda de cada dispersion 

plt.legend()

plt.show()