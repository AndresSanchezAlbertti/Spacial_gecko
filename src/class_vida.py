import pygame

from modo import *
class Vida(pygame.sprite.Sprite):
    def __init__(self,imagen,pos_x,pos_y,es_visible):
        super().__init__()
        self.imagen= pygame.image.load(imagen)
        self.tamanio = (50,50)
        self.imagen = pygame.transform.scale(self.imagen, self.tamanio)
        self.rect = self.imagen.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.es_visible = es_visible
    
        
    
    def animar (self,pantalla):
        if self.es_visible:
            pantalla.blit(self.imagen, self.rect)
    
    
    
    
    def eliminar_item(self,lista_item):
        lista_item.remove(self)
    def invisibilizar(self,):
        self.es_visible =False
    
     
    def update_vidas(self,pantalla):
        self.animar_item(pantalla)
    
    def dibujar_rect(self,pantalla):
        for item in self.lista_items:
            pygame.draw.rect(pantalla,"Blue", item.rect,2)