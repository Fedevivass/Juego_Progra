from funciones_para_matriz import *
import re
def obtener_lista_de_palabras(path):
    with open(path,"r",encoding="UTF-8") as archivo:
        lista_palabras = []
        for linea in archivo:
            palabras= re.split(",|\n",linea)
            palabras.pop()
            lista_palabras.append(palabras)
    return lista_palabras


def normalizar_datos(lista_palabras:list)->None:
    for palabra in lista_palabras:
        for i in range(len(palabra)):
            palabra[i] = palabra[i].lower()
    return lista_palabras

def crear_diccionario_categorias(lista_palabras):
    diccionario_categorias = {}
    for palabra in lista_palabras:
        categorias = palabra[0]
        if categorias not in diccionario_categorias:
            diccionario_categorias[categorias] = []
        diccionario_categorias[categorias].append(palabra)
    return diccionario_categorias

def crear_lista_de_elementos(lista_palabras:list,comienzo,final)->list:
    lista_de_elementos = []
    for i in range(comienzo,final):
        if lista_palabras[i][1] not in lista_de_elementos:
            lista_de_elementos.append(lista_palabras[i][1])
    return lista_de_elementos


def agregar_elementos_a_matriz(lista:list):
    matriz_de_elementos = []
    lista_palabras = lista
    for i in range(0,len(lista_palabras),4):
        matriz_de_elementos.append(lista_palabras[i:i+4])
    return matriz_de_elementos

def cargar_datos_de_archivo():
    pass



































# def agrupar_lista_de_elementos(lista_elementos: list) -> list:
#     listas_categorias = []
#     for _ in range(len(lista_elementos[0])):
#         listas_categorias.append([])

#     for elemento in lista_elementos:
#         for i in range(len(elemento)):
#             listas_categorias[i].append(elemento[i])

#     return listas_categorias