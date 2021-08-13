#CREADO POR JOHN ESTEBAN PULIDO SALINAS: J.PULIDOS@UNIANDES.EDU.CO
import matplotlib.pyplot as plt
import pandas as pd

#CONSTANTES
""" comida = alimento bacterias
    bacteria tipo 1 = [rapidez, cantidad, tope, realentizacion]
    bacteria tipo 1 = [rapidez, cantidad, tope, realentizacion]
    bacteria tipo 1 = [rapidez, cantidad, tope, realentizacion]
    rapidez: m/s
    cantidad: número de bacterias por tipo
    tope: número de bacterias en las cules pueden realentizarse
    realentizacion: baja de rapidez por alcanzar el tope
"""
def calcularSeleccionNatural():
    b1 = [4, 3, 10, 2, False]
    b2 = [3, 2, 8, 1, False]
    b3 = [2, 4, 9, 0, False]
    dist = 8
    b1c = []
    b2c = []
    b3c = []
    comidas = []
    for i in range(0, 1000, 100):
        comida = i
        b1c.append(b1[1])
        b2c.append(b2[1])
        b3c.append(b3[1])  
        comidas.append(i)
        for t in range(60):
            if b1[1] > b1[2] and b1[4] == False:
                b1[0] -= b1[3]
                b1[4] = True
            if b2[1] > b2[2] and b2[4] == False:
                b2[0] -= b2[3]
                b2[4] = True
            if b3[1] > b3[2] and b3[4] == False:
                b3[0] -= b3[3]
                b3[4] = True
            dist1 = b1[0]*t
            dist2 = b2[0]*t
            dist3 = b3[0]*t
            if comida != 0 and dist1 > dist:
                if comida >= b1[1]:
                    comida -= b1[1]
                    b1[1] = b1[1]*2
                else:
                    b1[1] -= comida
                    comida = 0
            if comida != 0 and dist2 > dist:
                if comida >= b2[1]:
                    comida -= b2[1]
                    b2[1] = b2[1]*2
                else:
                    b2[1] -= comida
                    comida = 0
            if comida != 0 and dist3 > dist:
                if comida >= b3[1]:
                    comida -= b3[1]
                    b3[1] = b3[1]*2
                else:
                    b3[1] -= comida
                    comida = 0
            if comida == 0:
                break
    print(comidas)
    print(b1c, b2c, b3c)
    plt.plot(comidas, b1c)
    plt.plot(comidas, b2c)
    plt.plot(comidas, b3c)
    plt.xlabel("Comida Por Minuto")
    plt.ylabel("Población de bacterias")
    plt.legend(["bacteria 1","bacteria 2","bacteria 3"])
    plt.show()  
    return None

calcularSeleccionNatural()

    

