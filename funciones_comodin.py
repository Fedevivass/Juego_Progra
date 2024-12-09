import random
from funciones_agrup import *
AZUL = "\033[94m"
RESET = "\033[0m"

def verificar_categoria(diccionario_categorias: dict, categoria_encontrada: str):

    while True:
        categoria_random = random.choice(list(diccionario_categorias))
        if categoria_random != categoria_encontrada:
            return categoria_random


def seleccionar_palabra_diferente(palabra_random_uno,palabra_random_dos,palabras):
    while palabra_random_dos == palabra_random_uno:
        palabra_random_dos = random.choice(palabras)
    
    return palabra_random_dos


def menu_comodines(lista_de_categorias:dict,categoria:str,estado_comodines:list,vidas,categorias_disponibles)-> int:
    while True:
        opcion = input("1.COMODIN: Otorga una categoria y una palabra\n2.COMODIN: Otorga dos palabras de una categoria\n3.COMODIN: Otorga una vida extra\n4.NO USAR NINGUN COMODIN\nElegir una opcion: ")
        match opcion:
            case "1":
                if not estado_comodines[0]:
                    revelar_comodin_categoria(lista_de_categorias, categoria,categorias_disponibles)
                    estado_comodines[0] = True
                    break
            case "2":
                if not estado_comodines[1]:
                    revelar_comodin_dos_palabras(lista_de_categorias, categoria,categorias_disponibles)
                    estado_comodines[1] = True
                    break
            case "3":
                if not estado_comodines[2]:
                    estado_comodines[2] = True
                    vidas +=1
                    break
            case "4":
                print("SALIENDO")
                break
    return vidas