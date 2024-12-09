from funciones_de_listas import *
from funciones_para_matriz import *
from funciones_datos_ingresados import *
from funciones_comodin import*
from funciones_agrup import *
import time
import os
os.system("cls")

ROJO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"

def inicio_de_juego(archivo_nivel,nivel, vidas, puntos, validacion_nombre,categoria_adivinada:int):

    """Inicia el juego , controlando las vidas,
    puntos, y el uso de comodines, hasta que el jugador gane o pierda.


Parámetros:
    archivo_nivel (list): Lista que contiene los archivos de nivel (por ejemplo, archivos de palabras por nivel).
    nivel (int): El nivel actual del juego.
    vidas (int): El número de vidas restantes del jugador.
    puntos (int): Los puntos acumulados por el jugador.
    validacion_nombre (str): El nombre del jugador.
    categoria_adivinada (list): Lista que lleva el control del número de categorías adivinadas.

    - Muestra el mensaje de bienvenida al nivel actual.
    - Obtiene las palabras y las categorías para el nivel actual.
    - Llama a varias funciones para gestionar la mecánica del juego, como adivinar palabras, usar comodines y verificar el estado del jugador.
    - Realiza el seguimiento de las vidas y puntos, y termina el juego cuando el jugador pierde todas las vidas o gana el juego.
    - Avanza a niveles superiores cuando se alcanzan los objetivos establecidos.
    
    Retorna:
    bool: `True` si el jugador desea seguir jugando después de completar el nivel, `False` si el jugador ha perdido o ganado.

    """

    lista_palabras = obtener_lista_de_palabras(archivo_nivel)
    lista_normalizada = normalizar_datos(lista_palabras)
    diccionario_cat = crear_diccionario_categorias(lista_palabras)
    lista_elementos = crear_lista_de_elementos(lista_normalizada,0,16)
    matriz_elementos = agregar_elementos_a_matriz(lista_elementos)



    resultado = identificar_categorias(matriz_elementos,diccionario_cat)
    print(resultado)



    print(f"Bienvenido al nivel {nivel}")
    matriz_desordenada = desordenar_matriz_total(matriz_elementos)
    print(f"{AMARILLO}")
    mostrar_matriz(matriz_desordenada)
    print(f"{RESET}")
    comodines_usados = [False, False, False]
    categoria_adivinada[0] = 0
    empezar = int(time.time())
    bandera = True
    bandera_dos = True
    bandera_return = True

    while bandera_return:
        print("-" * 80)
        lista_palabras_ingresadas = obtener_palabras_ingresadas(4)

        categoria_encontrada = identificar_categoria(lista_palabras_ingresadas, matriz_elementos, diccionario_cat)
        if categoria_encontrada:
            categoria_adivinada[0] += 1
            puntos[0] += 10
            vidas[0] = menu_comodines(diccionario_cat, categoria_encontrada, comodines_usados, vidas[0])
            print(f"{VERDE}Bien {validacion_nombre}, encontraste {categoria_encontrada}. Puntos: {puntos[0]}{RESET}")
            print("-" * 80)
        else:
            vidas[0] -= 1
            print(f"{ROJO}Perdiste una vida. Vidas restantes: {vidas[0]}{RESET}")

        if comodines_usados[0]:
            print("Usaste Comodin Uno")
        if comodines_usados[1]:
            print("Usaste Comodin Dos")
        if comodines_usados[2]:
            print(f"Ganaste una vida extra. Vidas: {vidas}")

        if vidas[0] <= 0:
            terminar = int(time.time()) - empezar
            gestionar_perdida(validacion_nombre, puntos[0], vidas[0], terminar)
            bandera_return = False
            return bandera_return

        if categoria_adivinada[0] == 4 and bandera:
            comodines_usados = [False, False, False]
            bandera = False
            lista_palabras = obtener_lista_de_palabras(archivo_nivel)
            lista_normalizada = normalizar_datos(lista_palabras)
            diccionario_cat = crear_diccionario_categorias(lista_palabras)
            lista_elementos = crear_lista_de_elementos(lista_normalizada,16,32)
            matriz_elementos = agregar_elementos_a_matriz(lista_elementos)


        if categoria_adivinada[0] == 8 and bandera_dos:
            comodines_usados = [False, False, False]
            bandera_dos = False
            lista_palabras = obtener_lista_de_palabras(archivo_nivel)
            lista_normalizada = normalizar_datos(lista_palabras)
            diccionario_cat = crear_diccionario_categorias(lista_palabras)
            lista_elementos = crear_lista_de_elementos(lista_normalizada,32,48)
            matriz_elementos = agregar_elementos_a_matriz(lista_elementos)


        if categoria_adivinada[0] == 12:
            bandera_return = True
            return bandera_return
        if puntos[0] == 600:
            terminar = int(time.time()) - empezar
            guarda_puntuacion(validacion_nombre, puntos[0], "Ganaste", terminar)
            print(f"TU TIEMPO FUE DE {terminar} SEGUNDOS")
            bandera_return = False
            return bandera_return



