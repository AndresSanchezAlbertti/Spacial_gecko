import pygame

from modo import *
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posicion_inicial, es_visible):
        # Inicialización de la clase (carga de imagen, configuración de rectángulos, etc.)
        super().__init__()
        self.image = pygame.image.load('aster/aster1.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0]
        self.rect.y = posicion_inicial[1]
        self.es_visible = True
        self.velocidad_caida = 5
        self.coordenadas =[(-20,10),(-20, 50),(-20,70),(-20,150), (-20,200),(-20,250),(-20,300),(-20,350), (-20,450),(-20, 500),(-20,550),(-20,600),(-20,700),(-20,850),(-20,950)]
        self.lista_asteroides =[]
        

    
    def caer(self):
        # Actualizar la posición vertical del asteroide
        self.rect.y += self.velocidad_caida
        # Si el asteroide llega al final de la pantalla, puedes reiniciar su posición o eliminarlo
        if self.rect.y > 0:
            self.rect.y += 5

    def animar_item (self,pantalla):
        
        if self.es_visible:
            pantalla.blit(self.image, self.rect)
            

    
