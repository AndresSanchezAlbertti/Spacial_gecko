import pygame
import random
from configuraciones import *
from class_personaje import *  
from class_enemigo import *
from class_plataforma import *
from class_plataformas_grandes import *
from class_item import *
from pygame.locals import *
from modo import *
from class_nivel import Nivel
from class_nivel_uno import *
from class_nivel_dos import *
from class_proyectil import *
from class_nivel_boss import *
from manejador_niveles import *
from gui.GUI_form_prueba import *
import sys

##################################
#def actualizar_pantalla (pantalla:tuple,un_personaje,fondo, lados_piso, plataforma,demo_proyectil):
#    lista_coordenadas = [(100,700), (300,500), (200,300)]
#    pantalla.blit(fondo,(0,0))
#    un_personaje.update(pantalla, lados_piso)
    #plataformas
#    for i in lista_coordenadas:
#       pass
        #pantalla.blit(plataforma,(x,y))
  
pygame.init()
lista_niveles = [nivel_uno(PANTALLA)]
form_principal = FormPrueba(PANTALLA, 200,200,900,350,"black","grey",5,True)
nivel_actual = nivel_uno(PANTALLA)

while True:
    RELOJ.tick(FPS)
    #reloj.tick(FPS)
    eventos = pygame.event.get()
    #demo_proyectil.trayectoria()
    for evento in eventos:
        if evento.type==pygame.QUIT:
            pygame.quit()    
            sys.exit(0)
            
    nivel_actual.update(eventos)
    #if nivel_actual.cantidad_enemigos == 0:
    #    indice_actual = lista_niveles.index(nivel_actual)
    #    siguiente_inidice = (indice_actual +1) % len(lista_niveles)    
    #    nivel_actual= lista_niveles[siguiente_inidice]
    #form_principal.update(eventos)
            #pygame.draw.rect(display,"Blue",plataforma.lados,2)
    pygame.display.update()