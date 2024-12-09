from funcion_de_main import *

flag_partida = input("¿Quieres jugar?: ").lower()
validacion_nombre = ingresar_nombre_usuario("Ingresar nombre: ", "Longitud no permitida, reingrese: ", 3, 13)

vidas = [3]
puntos = [0]
categoria_adivinada = [0]

while flag_partida == "si":
    nivel_actual = 1


    continuar = inicio_de_juego("Categorias.csv", nivel_actual, vidas, puntos, validacion_nombre,categoria_adivinada)

    if not continuar:
        print(f"Fin del juego en el nivel {nivel_actual}. Gracias por jugar.")
        puntajes_primeros()
        flag_partida = "no"
        break

    nivel_actual += 1 

    if flag_partida == "si":
        print("GANASTE EL JUEGO.")
        flag_partida = input("¿Quieres volver a jugar?: ").lower()
        if flag_partida == "si":
            nivel_actual = 1