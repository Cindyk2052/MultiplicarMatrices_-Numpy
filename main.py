import numpy as np
import sys

print("Bienvenido al PROGRAMA PARA MULTIPLICAR MATRICES\n")

fm1 = int(input("Ingrese el numero de filas de la matriz 1: "))
cm1 = int(input("Ingrese el numero de columnas de la matriz 1: "))

fm2 = int(input("\nIngrese el numero de filas de la matriz 2: "))
cm2 = int(input("Ingrese el numero de columnas de la matriz 2: "))

if cm1 != fm2:
  print("\n NO SE PUDEN MULTIPLICAR LAS MATRICES (DEBE SER IGUAL NUMERO DE COLUMNAS DE LA MATRIZ 1 Y NUMERO DE FILAS DE LA MATRIZ 2")
  sys.exit()

matriz1 = np.zeros((fm1, cm1))
matriz2 = np.zeros((fm2, cm2))
matrizresult = np.zeros((fm1, cm2))

print("\nIngrese los elementos de la matriz 1")
for f in range(0, fm1):
    for c in range(0, cm1):
        matriz1[(f, c)] = input("Elemento "+str(f + 1)+","+str(c + 1)+": ")


print("\nIngrese los elementos de la segunda matriz")
for f in range(0, fm2):
    for c in range(0, cm2):
        matriz2[(f, c)] = input("Elemento "+str(f + 1)+","+str(c + 1)+": ")

# Multiplicación
for f in range(0, fm1):
    for c in range(0, cm2):
        for k in range(0, fm2):
            matrizresult[f, c] += matriz1[f, k]*matriz2[k, c]

print("\nResultado: \n")
print(matrizresult)




