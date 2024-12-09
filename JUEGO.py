import pygame
from funciones_pygame import *
pygame.init()


BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL_CLARO = (0, 150, 255)
NEGRO = (0, 0, 0)
color_sombra = (20, 20, 20)


ventana_de_juego = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Agrupados")

icono_juego = pygame.image.load("iconojuegos.jpg")
pygame.display.set_icon(icono_juego)


ventana_de_juego.fill(BLANCO)


texto = " JUGAR "
cuadro = pygame.Rect(300, 250, 200, 50)

fuente = ajustar_tamano_fuente(texto, cuadro.width - 10, cuadro.height - 10)


flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False


    dibujar_sombra(ventana_de_juego, cuadro, color_sombra)


    dibujar_rectangulo_redondeado(ventana_de_juego, AZUL_CLARO, cuadro, 10)
    pygame.draw.rect(ventana_de_juego, NEGRO, cuadro, 2, border_radius=10)


    superficie_texto = fuente.render(texto, True, NEGRO)
    texto_x = cuadro.x + (cuadro.width - superficie_texto.get_width()) // 2
    texto_y = cuadro.y + (cuadro.height - superficie_texto.get_height()) // 2
    ventana_de_juego.blit(superficie_texto, (texto_x, texto_y))


    pygame.display.update()

# Salir de Pygame
pygame.quit()
