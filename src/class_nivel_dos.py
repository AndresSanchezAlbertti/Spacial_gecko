from class_nivel import *
from class_enemigo import *
from class_boss import *
from class_personaje import*
from class_vida import *
from pygame.locals import *
from modo import *
from class_plataforma import *
from class_plataformas_grandes import *
import pygame
def generar_pisos(imagen,coordenadas,lista_plataformas,lista_plataformas_dos):
    for i in range(len(coordenadas)):
        for coordenada in coordenadas:
            x = coordenada[0]
            y = coordenada[1]
            plataforma= Plataforma(imagen,5,(x, y),100)
            lista_plataformas.append(plataforma)
            lista_plataformas_dos.append(plataforma)

def generar_vidas(lista_vidas,imagen,lista_coordenadas,tamanio):
    for i in range(4):
        for coordenada in lista_coordenadas:
            vida = Vida(imagen,coordenada[0],coordenada[1],True)
            lista_vidas.append(vida)
def generar_coins(imagen,lista_coins,lista_coordenadas):
    for i in range(4):
        for coordenada in lista_coordenadas:
            coin = Item(imagen,coordenada[0],coordenada[1],True,False, (20,20))
            lista_coins.append(coin)       
def generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final):
        
        for i in range(len(lista_posicion_inicial)):
            enemigo = Enemigo(diccionario_animaciones,lista_posicion_inicial[i],lista_posicion_final[i],2)
            lista_enemigos.append(enemigo)


class nivel_dos_(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        W =pantalla.get_width()
        H = pantalla.get_height()
        ##FONDO###
        fondo = pygame.image.load("space_one.png")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        ##PERSONAJE###
        
        posicion_inicial = (H//2-200,W//2) 
        ###Plataformas###
        coordenadas_piso = [(0,550),(98,550),(490,550),(588,550),(686,550),(784,550),(882,550),(98,376), (196,376),(294,376), (392,376),(490,376),(588,376),(686,376),(784,376),(882,376),(12,432),(12,485),(0,181),(98,181), (196,181),(294,181), (392,181),(490,181),(588,181),(686,181),(784,181), (895,268),(899,326),(899,215),(13,71),(196,71),(294,71), (392,71),(490,71),(588,71),(686,71),(784,71), (895,71),(899,71),(899,71),(136,129),(315,502)]
        
        #################################################################################################
        
        
        ##ENEMIGOS###
        lista_posicion_inicial= [(848, 510),(842,330),(590,330)]
        lista_posicion_final=[(79,510),(590,330),(350,330)]
        lista_enemigos = []
        generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final)
        lista_coordenadas=[(870,12),(920,12),(965,12)]
        
        ##################################################
        

        display = pygame.display.set_mode((W,H))
        #PROYECTIL
        #demo_proyectil= Proyectil (player.lados["main"].top, player.lad)
        #lados_proyectil = obtener_rectangulo(demo_proyectil.rect)
        #Enemigos

        #PISO CON CLASES:
        piso = Plataforma("nivel_dos/plataforma_space.png",0,(0,550), 1000)
        



       # Esto devuelve un diccionario de lados que voy a recorrene en el loop para dibujarlos si yo quiero acceder solo a un lado debería poner lados_piso["bottom"] y si le agrego lados_piso["bottom"].top es la parte de arriba del bottom
        

        #Esta es la lista para las imagenes
        plataformas_clases_dos = []
        #El problema ahora es que tengo que hacer lo mismo con los pisos grandes
        #Esta es la lista para los rect
        plataformas_clases = []
        generar_pisos("nivel_dos/plataforma_space.png", coordenadas_piso,plataformas_clases_dos,plataformas_clases)
        
        #PISO
        #enemigo_uno= Enemigo("enemigo1.png", (622,527),(413,527),3)
        #enemigos = [enemigo_uno]

        #en sprites van a estar tdoos los elementos del juego

        #En enemigos van a ir todos los sprites de enemigos
        #plataforma
        
        # Calcula el ancho disponible para las plataformas (restando el espacio entre ellas)
        
        # Calcula las coordenadas x de cada plataforma

        #ENEMIGOS

        item_vida = Item("vida.png", 500,2,True,False,(30,30))
        item_combustible= Item("item_combustible.png", 64,397,True,False,(30,30))
        item_weapon = Item("weapon.png",47,49,False,False,(30,30))
        item_puerta_cerrada = Item("nivel_dos/puerta_cerrada.png",900,450,True,False,(100,100))
        item_puerta_abierta = Item("nivel_dos/puerta_abierta.png",900,450,False,False,(100,100))
        item_switch_prendido= Item("nivel_dos/switch_encendido.png",57,50,False,False,(70,70))
        item_switch_apagado = Item("nivel_dos/switch_apagade.png",57,50,True,False,(70,70))
        lista_items = [item_combustible,item_vida, item_weapon,item_puerta_abierta,item_puerta_cerrada,item_switch_prendido,item_switch_apagado]
        lista_vidas = []
        generar_vidas(lista_vidas,"vidas.png",lista_coordenadas,(30,30))
        coordenadas_coins=[(145,359),(250,359),(339,347),(443,346),(528,344),(635,350),(741,352),(836,344),(718,151),(630,148),(540,144),(444,149),(336,149)]
        lista_coins = []
        lista_asteroides = []
        generar_coins("coin_sprite.png",lista_coins,coordenadas_coins)
        jugador = Personaje ((50,50), diccionario_animaciones, posicion_inicial,10,lista_vidas,lista_asteroides)
        boss =Boss((50,50),diccionario_boss,(800,300),10,False)  
        
        super().__init__(fondo,display,jugador,piso, plataformas_clases,plataformas_clases_dos,lista_items,lista_enemigos, lista_vidas, lista_coins,boss,lista_asteroides)
