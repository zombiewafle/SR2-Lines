# Archivo creado para almanecar todas las operaciones 
#matematicas usadas en el documento gl.py


#producto punto

#Variables de prueba

import numpy as np
from array import array


a = [1,2,3]
b = [4,5,6]


def dotProduct(a,b):
    dotProduct = 0
    for x,y in zip(a,b):
        dotProduct = dotProduct + (x*y)
    
    #print(dotProduct)


#dotProduct(a,b)

#Funcion para sumar vectores de 3 elementos 
#Notas: Los vectores con una mayor cantidad de elementos, ejemplo: 
# a = [1,2,3,4] 
# El elemento 4 sera ignorado

def sumVectors(a,b):
    sub1 = a[0] + b[0]
    sub2 = a[1] + b[1]
    sub3 = a[2] + b[2]
    sub = [sub1,sub2,sub3]
    

   # print(i)

#sumVectors(a,b)


def subVectors(a,b):
    sub1 = a[0] - b[0]
    sub2 = a[1] - b[1]
    sub3 = a[2] - b[2]
    sub = np.array([sub1,sub2,sub3])
    
    #print(sub)

#subVectors(a,b)

def crossProduct(a,b):
    #A × B = (bz – cy)i + (cx – az)j + (ay – bx)k
    
    crossProduct1 = ((a[1])*(b[2])) - ((a[2])*(b[1]))
    crossProduct2 = ((a[2])*(b[0])) - ((a[0])*(b[2]))
    crossProduct3 = ((a[0])*(b[1])) - ((a[1])*(b[0]))

    crossProduct = np.array([crossProduct1 , crossProduct2 , crossProduct3])
    
    #print(np.array(crossProduct))

#crossProduct(a,b)
