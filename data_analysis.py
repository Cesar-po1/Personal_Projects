#Reto algebra-Cesar Ponce, Jaime Charaf, Pablo Figueroa
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import random
import requests
from playsound import playsound
import pandas as pd
import time

def main():
    
    matriz_orginal = np.loadtxt("ma1034-datos-sitprb3D.csv", dtype='f', delimiter=',',skiprows = 1) #lee el archivo
    matriz_centralizada, df = centralizar(matriz_orginal) #centraliza matriz original
    time.sleep(1)
    matriz_var = varianza(matriz_centralizada) #saca la matriz 3x3 de covarianza
    time.sleep(.5)
    vec_prop = vect_propios(matriz_var) #vector propio y valores propios
    time.sleep(.5)
    resultado = multiplicacion(matriz_centralizada,vec_prop) #multiplica matriz centralizada por vector propio
    min_max(df)#DataFrame con empleados de mejor y peor desempeño
    print("""
Para desplegar graficas presione enter
""")
    input("Press Enter to continue...")
    fin = graficar(resultado) #resultado grafico
    print()
    if fin == 0:
        print('Gracias por usar nuestro programa')
        exit(0)
    elif fin == 1:
        print('Error')
        exit(1)
        
def centralizar(matriz):
    prom1=0
    prom0=0
    prom2=0

    for line in matriz:
        prom0+= line[0]
        prom1+= line[1]
        prom2+= line[2]

    prom0= prom0 / len(matriz)  
    prom1= prom1 / len(matriz)
    prom2= prom2 / len(matriz)  #promedio de cada columna
    i = 0
    for line in matriz:
        line[0] -= prom0
        line[1] -= prom1
        line[2] -= prom2 #resta el promedio de la columna a cada valor de su columna
    print('Matriz Centralizada')
    A = []
    B = []
    C = []
    for line in matriz:
        A.append(line[0])  #crea matriz ind para cada indicador
        B.append(line[1])
        C.append(line[2])
    #print(A)
    dataframe = {'ind1' : A,
                 'ind2' : B,
                 'ind3' : C
                 }
    df = pd.DataFrame(dataframe, columns = ['ind1','ind2','ind3'],index=list(range(1, 201, )))

    print (df)    
    return (matriz,df)

def varianza(matriz):
    A = []
    B = []
    C = []
    for line in matriz: #hace una matriz de todos los valores individuales
        A.append(line[0])
        B.append(line[1])
        C.append(line[2]) 
        
    data = np.array([A,B,C]) #juntas las tres columnas

    covMatrix = np.cov(data,bias=True)  #saca la matriz 3x3 de covarianza
    print()
    print('Matriz covarianza y varianza')
    print(covMatrix)
    print()
    return(covMatrix)

def vect_propios(matriz):
    
    L, V = np.linalg.eig(matriz) #saca valores propios y vectores propios 
    print('Valores propios')
    print(L)
    print('Vectores propios')
    print(V)
    
    tot = L[0]+L[1]+L[2]
    
    por_v0 = (L[0]*100)/tot
    por_v1 = (L[1]*100)/tot
    por_v2 = (L[2]*100)/tot #convierte a porcentaje los valores propios
    
    print("""
Porcentaje de varianza ind.1 = %f
Porcentaje de varianza ind.2 = %f
Porcentaje de varianza ind.3 = %f 
            """
            %
          (por_v0,por_v1,por_v2))
        
    return(V)

def multiplicacion(matriz,vec):

    mult = np.dot(matriz,vec) #multiplica los vectores propios por la matriz centralizada
    
    return(mult)

def graficar(n):

    A = []
    B = []
    C = []
    for line in n:
        A.append(line[0])  #crea matriz ind para cada indicador
        B.append(line[1])
        C.append(line[2])
    
    sequence_containing_x_vals = A
    sequence_containing_y_vals = B
    sequence_containing_z_vals = C  #asigna valores a graficar
    
    fig = plt.figure()
    ax = Axes3D(fig)  #para grafica 3D
    ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
    ax.set(xlabel ='ind 1', ylabel ='ind 2', zlabel='ind 3') #setup grafico 3D
    #plt.show()
    
    plt.figure('Grafico 1')   #primer grafica
    plt.plot(sequence_containing_x_vals,sequence_containing_y_vals,'o',color='r') 
    plt.xlabel('ind 1')
    plt.ylabel('ind 2')
    plt.title('Comparacion ind 1 e ind 2')
    #plt.show()
    
    plt.figure('Grafico 2')    #segunda grafica
    plt.plot(sequence_containing_x_vals,sequence_containing_x_vals,'o',color='g')
    plt.xlabel('ind 1')
    plt.ylabel('ind 1')
    plt.title('Comparacion ind 1 e ind 1')
    
    
    if (plt.show()): #imprime todas las graficas
        return 1
    else:
        return 0
    
def min_max(df):
    print("""
Se obtienen los valores absolutos de los indicadores y debido a que el indicador 1 es el que mas
influye el los trabajadores solo se tomara en cuenta este.

A continuacion se presenta la lista con los trabajadores con el peor y mejor en este orden

""")
    time.sleep(5)
    absolut = df.abs()
    sorte = absolut.sort_values(by= ['ind1'])
    print(sorte)
    print("""

A continuacion se presenta el trabajador con el mejor desempeño y sus indicadores
""")
    print(sorte.iloc[[0]])
    print("""

A continuacion se presenta el trabajador con el peor desempeño y sus indicadores
""")
    print(sorte.iloc[[len(sorte)-1]])
      
main()