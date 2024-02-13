from class_nivel import *
from class_enemigo import *
from class_personaje import*
from class_nivel_dos import *
from pygame.locals import *
from modo import *
from configuraciones import *
from class_boss import *
from class_vida import *
from class_plataforma import *
from clase_asteroides import *
from class_plataformas_grandes import *
import pygame
def generar_asteroides(lista_asteroides, lista_posicion_inicial):
    for i in range(len(lista_posicion_inicial)):
            enemigo = Asteroide(lista_posicion_inicial[i],True)
            lista_asteroides.append(enemigo)
def generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final):
        
        for i in range(len(lista_posicion_inicial)):
            enemigo = Enemigo(diccionario_animaciones,lista_posicion_inicial[i],lista_posicion_final[i],2)
            lista_enemigos.append(enemigo)
def generar_coins(lista_vidas,imagen,lista_coordenadas,tamanio):
    for i in range(4):
        for coordenada in lista_coordenadas:
            vida = Item(imagen,coordenada[0],coordenada[1],True,False,tamanio)
            lista_vidas.append(vida)
def generar_vidas(lista_vidas,imagen,lista_coordenadas,tamanio):
    for i in range(4):
        for coordenada in lista_coordenadas:
            vida = Vida(imagen,coordenada[0],coordenada[1],True)
            lista_vidas.append(vida)

class nivel_boss(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        W =pantalla.get_width()
        H = pantalla.get_height()
        ##FONDO###
        fondo = pygame.image.load("nivel_boss/back_gran_finale.png")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        ##PERSONAJE###
        tamanio= (50,50)
        posicion_inicial = (H//2,0) 
        

        ##ENEMIGOS###
        lista_posicion_inicial= [(848, 510),(842,330),(590,330),(142,327)]
        lista_posicion_final=[(79,510),(590,330),(350,330),(264,327)]
        
        #generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final)
        lista_coordenadas=[(870,12),(920,12),(965,12)]
        
        ##################################################
        display = pygame.display.set_mode((W,H))
        #PROYECTIL
        #demo_proyectil= Proyectil (player.lados["main"].top, player.lad)
        #lados_proyectil = obtener_rectangulo(demo_proyectil.rect)
        #Enemigos

        #PISO CON CLASES:
        piso = Plataforma("piso.png",0,(0,550), 1000)
       

        #Esta es la lista para las imagenes
        plataformas_clases_dos = [
                        
                        
        ]
        #El problema ahora es que tengo que hacer lo mismo con los pisos grandes
        #Esta es la lista para los rect
        plataformas_clases = [
                        piso
                        ]
        plataformasw_1_rec = [piso.imagen]
        #PISO
        #enemigo_uno= Enemigo("enemigo1.png", (622,527),(413,527),3)
        #enemigos = [enemigo_uno]

        #en sprites van a estar tdoos los elementos del juego

        #En enemigos van a ir todos los sprites de enemigos
        #plataforma
        numero_plataformas = 4
        espacio_entre_plataformas = 50
        # Calcula el ancho disponible para las plataformas (restando el espacio entre ellas)
        ancho_disponible = W - (numero_plataformas - 1) * espacio_entre_plataformas
        # Calcula el ancho de cada plataforma
        ancho_plataforma = W / numero_plataformas
        rectangulos_plataformas = []
        # Calcula las coordenadas x de cada plataforma
        #ENEMIGOs
        plataformas_lados  = []

        item_vida = Item("vida.png", 800,300,True,False,(30,30))
        item_combustible= Item("item_combustible.png", 373,4,True,False,(30,30))
        item_weapon = Item("weapon.png",39,126,False,False,(30,30))
        lista_items = [item_combustible,item_vida, item_weapon]
        lista_vidas = []
        generar_vidas(lista_vidas,"vidas.png",lista_coordenadas,(30,30))
        lista_asteroides = []
        posicion_inicial_asteroides= [(-20,10),(-20, 50),(-20,70),(-20,150), (-20,200),(-20,250),(-20,300),(-20,350), (-20,450),(-20, 500),(-20,550),(-20,600),(-20,700),(-20,850),(-20,950)]
        generar_asteroides(lista_asteroides,posicion_inicial_asteroides)
       
        coordenadas_coins=[(16,266),(105,266),(280,294),(339,461),(260,497),(522,401),(588,359),(651,317),(720,277),(799,214)]
        lista_coins = []
        lista_plataformas =[]
        lista_plataformas_dos =[]
        generar_pisos("plataforma_boss.png", coordenadas_coins,lista_plataformas, lista_plataformas_dos )
        lista_enemigos= []
        lista_plataformas.append(piso)
        jugador = Personaje (tamanio, diccionario_animaciones, posicion_inicial,10,lista_vidas)
        boss =Boss((250,250),diccionario_boss,(800,300),10,True,lista_asteroides)
        super().__init__(fondo,display,jugador,piso,lista_plataformas,lista_plataformas_dos, lista_items,lista_enemigos, lista_vidas, lista_coins,boss,lista_asteroides)
