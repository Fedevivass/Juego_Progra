from funciones_de_listas import *
from funciones_para_matriz import *
import json
AMARILLO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"

def identificar_categorias(matriz, palabras_clave):
    categorias_identificadas = {}

    for fila in matriz:
        # Normalizar cada elemento de la fila
        fila_normalizada = [elemento.lower() for elemento in fila]
        for categoria, claves in palabras_clave.items():
            # Normalizar cada palabra clave
            claves_normalizadas = [clave.lower() for clave in claves]
            # Verificar si todos los elementos están en las claves
            if all(elemento in claves_normalizadas for elemento in fila_normalizada):
                categorias_identificadas[categoria] = fila
                break  # Salimos si ya identificamos la categoría para esa fila

    return categorias_identificadas


def identificar_categoria(lista_palabras_ingresadas: list, lista:list, diccionario_categorias:dict):
    lista_categorias = list(diccionario_categorias)
    for i in range(len(lista)):
        if set(lista_palabras_ingresadas) == set(lista[i]):
            return lista_categorias[i]
    return None


def gestionar_perdida(nombre: str, puntos: int, vidas: int, termino):
    """Maneja el estado cuando el jugador pierde, guarda la puntuación y permite decidir si desea continuar jugando.

    Args:
        nombre (str): El nombre del jugador
        puntos (int): La cantidad de puntos obtenidos por el jugador
        vidas (int): El número de vidas restantes del jugador
        termino (type): variable relacionada al término del juego

    Returns:
        bool: True si el jugador desea seguir jugando, False si decide no continuar.
    """
    guarda_puntuacion(nombre, puntos, "perdio", termino)
    print(f"PERDISTE. VIDAS: {vidas}")
    continuar_jugando = input("¿Desea seguir jugando?: ") == "si"

    if continuar_jugando:
        vidas = 3

    return continuar_jugando

def guardar_puntuacion(nombre, puntos, gano, tiempo):
    datos = {"nombre": nombre, "puntos": puntos, "gano": gano, "tiempo": tiempo}
    try:
        with open("PRUEBA_PUNTAJE.json", "r") as archivo:
            puntuaciones = json.load(archivo)
    except (FileNotFoundError):  
        puntuaciones = []
    except (json.JSONDecodeError):
        puntuaciones = []
    
    puntuaciones.append(datos)  
    
    with open("PRUEBA_PUNTAJE.json", "w") as archivo:
        json.dump(puntuaciones, archivo, indent=4)

def guarda_puntuacion(nombre, puntos, gano, tiempo):
    """_summary_

    Args:
        nombre (str): nombre del jugador
        puntos (int): Los puntos obtenidos por el jugador.
        gano (str): Indica si el jugador ganó o no.
        tiempo (int): El tiempo que tardó el jugador en completar el juego.
    """
    
    datos = {"nombre": nombre, "puntos": puntos, "gano": gano, "tiempo": tiempo}
    
    try:
        with open("puntaje_jugadores.json", "r") as archivo:
            puntuaciones = json.load(archivo)
    except (FileNotFoundError):  
        puntuaciones = []
    except (json.JSONDecodeError):
        puntuaciones = []
    
    puntuaciones.append(datos)  
    
    with open("puntaje_jugadores.json", "w") as archivo:
        json.dump(puntuaciones, archivo, indent=4) 



