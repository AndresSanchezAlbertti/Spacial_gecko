import pygame

from modo import *
class Item(pygame.sprite.Sprite):
    def __init__(self,imagen,pos_x,pos_y,es_visible,esta_coleccionado,tamanio:tuple):
        super().__init__()
        self.imagen= pygame.image.load(imagen)
        self.tamanio = tamanio
        self.imagen = pygame.transform.scale(self.imagen, self.tamanio)
        self.rect = self.imagen.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.es_visible = es_visible
        self.coleccionado= esta_coleccionado
        self.otorga_puntaje = True
        
    
    def animar_item (self,pantalla):
        
        if self.es_visible:
            pantalla.blit(self.imagen, self.rect)
    def detectar_colision_item(self,lista_item,jugador):
        colision= False
        if jugador.lados["main"].colliderect(self.rect):
                
            self.es_visible = False
            self.coleccionado = True
            
            colision= True
        
        return colision
    
    def detectar_col_coin(self,lista_item,jugador):
        
        colision= False
        if jugador.lados["main"].colliderect(self.rect):
            
            self.es_visible = False
            self.coleccionado = True
            
            colision= True
        
        return colision
    def eliminar_item(self,lista_item):
        lista_item.remove(self)
    def invisibilizar(self,lista_):
        self.es_visible =False
    def quitar_puntaje(self):
        self.otorga_puntaje = False
     

    def coleccionar_item(self):
        self.coleccionado =True 
                    
    
    def dibujar_rect(self,pantalla):
        for item in self.lista_items:
            pygame.draw.rect(pantalla,"Blue", item.rect,2)
    
    
                
    
                

    



        
                
                
