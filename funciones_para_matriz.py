import random

import json

def agregar_elementos_a_matriz(lista:list):

    matriz_de_elementos = []
    lista_palabras = lista
    for i in range(0,len(lista_palabras),4):
        matriz_de_elementos.append(lista_palabras[i:i+4])
    return matriz_de_elementos

def desordenar_matriz_total(matriz):
    elementos = []
    for fila in matriz:
        for elemento in fila:
            elementos.append(elemento)
    desordenar_elementos(elementos)

    matriz_desordenada = llenar_matriz_con_elementos(matriz,elementos)

    return matriz_desordenada

def mostrar_matriz(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " | ")
        print()

def puntajes_primeros():
    with open('PRUEBA_PUNTAJE.json', 'r') as archivo:
        datos = json.load(archivo)
    datos_ordenados = sorted(datos, key=lambda jugadores: jugadores['puntos'], reverse=True)
    mejores_9 = datos_ordenados[:9]
    matriz = []
    for jugador in mejores_9:
        lista = []
        nombre_jugador = jugador['nombre']
        puntaje_jugador = jugador['puntos']
        lista.append(nombre_jugador)
        lista.append(puntaje_jugador)
        matriz.append(lista)
    print("Matriz de los 9 con más puntos:")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " | ")
        print()

def inicializar_matriz(cantidad_filas:int , cantidad_columnas:int, valor_inicial:any) -> list :
    matriz = []

    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas 
        matriz += [fila]
    return matriz

def desordenar_elementos(elementos):
    for i in range(len(elementos)):
        j = random.randint(0, len(elementos) - 1)
        elementos[i], elementos[j] = elementos[j], elementos[i]
    return elementos

def llenar_matriz_con_elementos(matriz,elementos):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_desordenada = inicializar_matriz(4,4,0)

    index = 0
    for i in range(filas):
        for j in range(columnas):
            matriz_desordenada[i][j] = elementos[index]
            index += 1
    
    return matriz_desordenada

