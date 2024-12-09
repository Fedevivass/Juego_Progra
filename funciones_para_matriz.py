import random

import json
def agregar_elementos_a_matriz(lista:list):
    """Agrupa los elementos de una lista en sublistas de tamaño 4 y las organiza en una matriz.
    Parámetros:
    lista (list): Una lista de elementos que se agruparán en sublistas de tamaño 4.

    Retorna:
    list: Una lista de sublistas, donde cada sublista contiene hasta 4 elementos de la lista original.
    """


def agregar_elementos_a_matriz(lista:list):

    matriz_de_elementos = []
    lista_palabras = lista
    for i in range(0,len(lista_palabras),4):
        matriz_de_elementos.append(lista_palabras[i:i+4])
    return matriz_de_elementos

def desordenar_matriz_total(matriz):

    """Desordena los elementos de una matriz de manera aleatoria y devuelve una nueva matriz con los elementos desordenados.

    La función toma una matriz y extrae todos sus elementos en una lista plana. Luego, desordena los elementos 
    de manera aleatoria y los reorganiza en una nueva matriz con las mismas dimensiones que la original.

    Parámetros:
    matriz (list): Una lista de listas (matriz) que contiene los elementos a desordenar.

    Retorna:
    list: Una nueva matriz con las mismas dimensiones que la original, pero con los elementos desordenados.
    """

    elementos = []
    for fila in matriz:
        for elemento in fila:
            elementos.append(elemento)
    desordenar_elementos(elementos)

    matriz_desordenada = llenar_matriz_con_elementos(matriz,elementos)

    return matriz_desordenada

def mostrar_matriz(matriz:list):
    """ Muestra la matriz en la consola, imprimiendo cada elemento de forma ordenada.
    Parámetros:
    matriz (list): Una matriz que contiene los elementos a mostrar en la consola.
    Retorna:
    None: La función solo imprime la matriz en la consola, no retorna ningún valor.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " | ")
        print()

def puntajes_primeros():
    """Lee un archivo JSON con los puntajes de los jugadores, ordena los jugadores según sus puntos de mayor a menor,
    selecciona a los 9 primeros jugadores con más puntos y los muestra en una matriz.
    No recibe parámetros y no retorna ningún valor.

    Requiere:
    - Un archivo `puntaje_jugadores.json` que contenga los puntajes de los jugadores.
    - La función `mostrar_matriz` para mostrar la matriz resultante.
    """
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
    # meter elementos dentro de la matriz 
    for _ in range(cantidad_filas): #el for  determina la cantidad de filas 
        fila = [valor_inicial] * cantidad_columnas # cree una fila , no esta dentro de la matriz 
        matriz += [fila] # le agregue la fila a la matriz 
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
