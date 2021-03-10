from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
def costo_and(w1,w2):
                  # x0 x1 x2
    x = np.matrix([[1, 1, 1],
                   [1, 1, 0],
                   [1, 0, 1],
                   [1, 0, 0]]
                  )
    y = np.matrix([[1],
                   [0],
                   [0],
                   [0]
                   ])
    w = np.matrix([[0.5],
                   [w1],
                   [w2]
                   ])

    h = np.dot(x,w) 
    print(h)
   
    matriz_resta = h-y
    matriz_al_cuadrado = np.power(matriz_resta,2)
    suma = np.sum(matriz_al_cuadrado)
    r_final_escalar = suma/2
    return(r_final_escalar)

x  = np.linspace(-4,4,100)
y = np.linspace(-4,4,100)

x1 ,y1 = np.meshgrid(x,y) 
funcion_and = costo_and(x1,y1) #CostoAND

#AND
imagen = plt.figure()
subImagen = imagen.gca(projection='3d',title='AND')
subImagen.plot_surface(x1,y1,funcion_and,cmap=cm.coolwarm) 



def costo_or(w1,w2):
                  # x0 x1 x2
    x = np.matrix([[1, 1, 1],
                   [1, 1, 0],
                   [1, 0, 1],
                   [1, 0, 0]]
                  )
    y = np.matrix([[1],
                   [1],
                   [1],
                   [0]
                   ])
    w = np.matrix([[0.5],
                   [w1],
                   [w2]
                   ])

    h = np.dot(x,w) 

    matriz_resta = h-y
    matriz_al_cuadrado = np.power(matriz_resta,2)
    suma = np.sum(matriz_al_cuadrado)
    r_final_escalar = suma/2
    return(r_final_escalar)

funcion_or = costo_or(x1,y1) #CostoOR


#OR
imagen2 = plt.figure()
subImagen2 = imagen2.gca(projection='3d',title='OR')
subImagen2.plot_surface(x1,y1,funcion_or,cmap=cm.coolwarm)


plt.show()

