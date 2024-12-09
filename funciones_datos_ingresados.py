
def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int)->str:
    """Solicita al usuario que ingrese su nombre, asegurándose de que su longitud esté dentro de los límites especificados.

    Parámetros:
    mensaje (str): El mensaje que se mostrará al usuario para solicitar el nombre.
    mensaje_error (str): El mensaje que se mostrará si el nombre ingresado no cumple con las restricciones de longitud.
    minimo_len (int): La longitud mínima permitida para el nombre.
    maximo_len (int): La longitud máxima permitida para el nombre.

    Retorna:
    str: El nombre ingresado por el usuario que cumple con las restricciones de longitud.
    """
    nombre_ingresado = input(mensaje)
    while len(nombre_ingresado) < minimo_len or len(nombre_ingresado) > maximo_len:
        nombre_ingresado = input(mensaje_error)
    return nombre_ingresado

def obtener_palabras_ingresadas(cantidad):

    """Solicita al usuario que ingrese una cantidad específica de palabras y las almacena en una lista.

    Parámetros:
    cantidad (int): La cantidad de palabras que el usuario debe ingresar.

    Retorna:
    list: Una lista que contiene las palabras ingresadas por el usuario.
    """


    lista_palabras = []
    for _ in range(cantidad):
        palabra = input("Ingresa la palabra: ")
        lista_palabras.append(palabra)
    return lista_palabras