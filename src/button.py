import pygame
from configuraciones import *

class Boton:
    def __init__(self, x, y, ancho, alto, color, texto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
        self.texto = texto
        self.font = pygame.font.Font(None, 36)
        
    def dibujar(self):
        pygame.draw.rect(PANTALLA, self.color, self.rect)
        texto = self.font.render(self.texto, True, (255,255,255))
        texto_rect = texto.get_rect(center=self.rect.center)
        PANTALLA.blit(texto, texto_rect)