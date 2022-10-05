#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:13:33 2022

@author: cristhiamdaniel
"""

# Importamos las librerias
import time
import matplotlib.pyplot as plt
import pandas as pd

# Funcion recursiva
def binomialC1(n, k):
	if k > n:
		return 0
	if k == 0 or k == n:
		return 1
	# Recursive Call
	return binomialC1(n-1, k-1) + binomialC1(n-1, k)

# Funcion Programacion Dinamica
def binomialC2(n, k):
    C = [[0 for x in range(k + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1

            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]

# Funcion Programacion Dinamica mejorada
def binomialC3(n, k):
    # Declaring an empty array
    C = [0 for i in range(k + 1)]
    C[0] = 1  # since nC0 is 1

    for i in range(1, n + 1):

        # Compute next row of pascal triangle using
        # the previous row
        j = min(i, k)
        while (j > 0):
            C[j] = C[j] + C[j - 1]
            j -= 1

    return C[k]

def getData(N_input):
    
    # Datos de entrada. Valores fijos de N:
    #N_input = [3,5,7,10,15]
    
    # Dataframe vacio
    df = pd.DataFrame()
    
    # Lista de tiempos de ejecucion vacia
    tiempos1 = [] # Funcion recursiva
    tiempos2 = [] # Funcion PD
    tiempos3 = [] # Funcion PD mejorada
    
    # Listas de terminos de n y k vacios:
    N = []
    K = []
    
    # Lista de coeficientes binomiales
    C1 = []
    C2 = []
    C3 = []
    
    ''' Bucle para calcular los tiempos de ejecucion
    para cada n se tiene los valores de k que van de 0 a n.
    Se calcula por lo tanto:
    (3+1) + (5+1) + (7+1) + (10+1) + (15+1) = 45 coeficientes binomiales
    Por lo tanto habra 45 tiempos de ejecucion'''
    
    for i in N_input:
        for j in range(i+1):
            
            ###########################
            t0 = time.time()
            coef1 = binomialC1(i,j)
            t1 = time.time()
            T1 = t1-t0
            ###########################
            t2 = time.time()
            coef2 = binomialC2(i,j)
            t3 = time.time()
            T2 = t3-t2
            ###########################
            t4 = time.time()
            coef3 = binomialC3(i,j)
            t5 = time.time()
            T3 = t5-t4
            ###########################
            
            # Anadir elementos a las listas:
            tiempos1.append(T1)
            tiempos2.append(T2)
            tiempos3.append(T3)
            ###########################
            C1.append(coef1)
            C2.append(coef2)
            C3.append(coef3)
            ###########################
            K.append(j)
            N.append(i)
    
    
    df['n'] = N
    df['k'] = K
    df['C(n,k) - Recursivo'] = C1
    df['C(n,k) - PD'] = C2
    df['C(n,k) - PD Mejorado'] = C3
    df['Tiempo Ejecucion - Recursivo'] = tiempos1
    df['Tiempo Ejecucion - PD'] = tiempos2
    df['Tiempo Ejecucion - PD Mejorado'] = tiempos3
    
    
    return df

def extraerDF(df, x):
    df_filter = df[df["n"] == x]
    return df_filter

def graficar(x,y1,y2,y3,n):
    plt.plot(x,y1, marker = "o", label = "F. recursivo")
    plt.plot(x,y2, marker = "v", label = "F. PD")
    plt.plot(x,y3, marker = "*", label = "F. PD mejorado")
    plt.grid()
    plt.legend()
    plt.title(f"Coeficientes binomiales para N={n}")
    plt.xlabel("K")
    plt.ylabel("tiempos de ejecucion")
    plt.savefig(f"figura_N{n}.png")
    plt.clf()
    #plt.show()
    
def main():
    global data, data_n3, data_n5, data_n7, data_n10, data_n15
    
    
    N_input = []
    cantidad = int(input("Cuantas graficas necesitas: "))
    for i in range(cantidad):
        numero = int(input("ingresa el termino N: "))
        N_input.append(numero)
        
        data = getData(N_input)
        data_n =  extraerDF(data, numero)
        
        x = data_n["k"]
        y1 = data_n['Tiempo Ejecucion - Recursivo']
        y2 = data_n['Tiempo Ejecucion - PD']
        y3 = data_n['Tiempo Ejecucion - PD Mejorado']
        graficar(x,y1,y2,y3,numero)

if __name__ == "__main__":
    main()