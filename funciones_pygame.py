import pygame
NEGRO = (0,0,0)
def dibujar_rectangulo_redondeado(superficie, color, rect, radio):
    pygame.draw.rect(superficie, color, rect, border_radius=radio)


def dibujar_sombra(superficie, rect, color_sombra, desplazamiento=4, radio=10):
    sombra_rect = rect.move(desplazamiento, desplazamiento)
    dibujar_rectangulo_redondeado(superficie, color_sombra, sombra_rect, radio)


def ajustar_tamano_fuente(texto, ancho_maximo, alto_maximo):
    tamano = 60
    while True:
        fuente_temporal = pygame.font.SysFont("consola", tamano)
        superficie_texto = fuente_temporal.render(texto, True, NEGRO)
        if superficie_texto.get_width() <= ancho_maximo and superficie_texto.get_height() <= alto_maximo:
            return fuente_temporal
        tamano -= 1
        if tamano < 10: 
            break
    return pygame.font.SysFont("consola", 10) 