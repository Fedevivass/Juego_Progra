import random

AZUL = "\033[94m"
RESET = "\033[0m"

def verificar_categoria(diccionario_categorias: dict, categoria_encontrada: str):

    """Verifica y selecciona una categoría aleatoria del diccionario que no sea la categoría ya encontrada.

    Parámetros:
    diccionario_categorias (dict): Diccionario que contiene las categorías como claves.
    categoria_encontrada (str): La categoría que ya ha sido encontrada y que no debe ser seleccionada.

    Retorna:
    str: Una categoría aleatoria del diccionario que no sea igual a la categoría ya encontrada.
    """


    while True:
        categoria_random = random.choice(list(diccionario_categorias))
        if categoria_random != categoria_encontrada:
            return categoria_random


def revelar_comodin_categoria(diccionario_categorias: dict, categoria_encontrada: str) -> bool:

    """utiliza un comodín para revelar una palabra aleatoria de una categoría diferente a la ya encontrada.

    Parámetros:
    diccionario_categorias (dict): Diccionario de categorías donde cada categoría está asociada a una lista de palabras.
    categoria_encontrada (str): La categoría que ya ha sido encontrada y que no debe ser utilizada por el comodín.

    Retorna:
    bool: `True` si se reveló una categoría y una palabra aleatoria, siempre devuelve `True` en este caso.
    """


    categoria_random = verificar_categoria(diccionario_categorias, categoria_encontrada)

    palabra_random = random.choice(diccionario_categorias[categoria_random])
    print(f"{AZUL}Categoría: {categoria_random},Elemento:{palabra_random[1]}{RESET}")


def revelar_comodin_dos_palabras(diccionario_categorias: dict, categoria_encontrada: str):

    """Utiliza un comodín para revelar dos palabras aleatorias de una categoría diferente a la ya encontrada.

    Parámetros:
    diccionario_categorias (dict): Diccionario de categorías donde cada categoría está asociada a una lista de palabras.
    categoria_encontrada (str): La categoría que ya ha sido encontrada y que no debe ser utilizada por el comodín.

    Retorna:
    None: La función no retorna ningún valor, solo muestra en consola las dos palabras reveladas.
    """

    categoria_random = verificar_categoria(diccionario_categorias, categoria_encontrada)

    palabras = diccionario_categorias[categoria_random]
    palabra_random_uno = random.choice(palabras)
    palabra_random_dos = random.choice(palabras)

    palabra_random_dos = seleccionar_palabra_diferente(palabra_random_uno,palabra_random_dos,palabras)


    print(f"{AZUL}Por usar el comodín te damos estos dos elementos: {palabra_random_uno[1]}, {palabra_random_dos[1]}{RESET}")

def seleccionar_palabra_diferente(palabra_random_uno,palabra_random_dos,palabras):
    while palabra_random_dos == palabra_random_uno:
        palabra_random_dos = random.choice(palabras)
    
    return palabra_random_dos

def menu_comodines(lista_de_categorias:dict,categoria:str,estado_comodines:list,vidas)-> int:

    """Muestra un menú para que el jugador elija entre tres comodines disponibles o no usar ninguno.

    Parámetros:
    lista_de_categorias (dict): Diccionario de categorías
    categoria (str): La categoría actual que se está jugando.
    estado_comodines (list): Lista de estados que indica si cada comodín ya ha sido utilizado (True/False).
    vidas (int): El número de vidas restantes del jugador.

    Retorna:
    int: El número actualizado de vidas después de usar un comodín (si se usa el comodín tres, incrementa las vidas).
    """


    while True:
        opcion = input("1.COMODIN UNO\n2.COMODIN DOS\n3.COMODIN TRES\n4.NO USAR NINGUN COMODIN\nElegir una opcion: ")
        match opcion:
            case "1":
                if not estado_comodines[0]:
                    revelar_comodin_categoria(lista_de_categorias, categoria)
                    estado_comodines[0] = True
                    break
            case "2":
                if not estado_comodines[1]:
                    revelar_comodin_dos_palabras(lista_de_categorias, categoria)
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