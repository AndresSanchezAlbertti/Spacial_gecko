import pygame
from pygame.locals import *
from class_personaje import *

class Proyectil(pygame.sprite.Sprite):
    def __init__(self,imagen, pos_x, pos_y,direccion):
        pygame.sprite.Sprite.__init__(self)
        self.imagen= pygame.image.load(imagen)
        self.rect=self.imagen.get_rect()
        self.velocidadDisparo = 10
        self.rect.centerx=pos_x
        self.rect.centery= pos_y
        self.direccion = direccion #-1 para izq 1 para derecha
        
    def eliminar_disparo(self,lista_disparo):
        lista_disparo.remove(self)

        

    def dibujar_rect(self,pantalla,un_jugador):
        for proyectil in un_jugador.listaDisparo:
            pygame.draw.rect(pantalla,"Blue", proyectil.rect,0)
    def blitear_proyectil(self,pantalla):
        
        pantalla.blit(self.imagen,(self.rect.centerx, self.rect.centery) )
    def trayectoria(self):
        if self.direccion == 1:
            self.rect.centerx += self.velocidadDisparo
        elif self.direccion == -1:
            self.rect.centerx -= self.velocidadDisparo
    def update(self,pantalla):
        # Mover el proyectil en la dirección hacia la derecha
        self.trayectoria()
        self.blitear_proyectil(pantalla)
        
    

        
    
   


