from class_nivel import *
from class_vida import *
from class_enemigo import *
from class_personaje import*
from pygame.locals import *

from modo import *
from class_plataforma import *
from class_plataformas_grandes import *
import pygame

def generar_lista_enemigos(lista_enemigos,lista_posicion_inicial,lista_posicion_final):
        
        for i in range(len(lista_posicion_inicial)):
            enemigo = Enemigo(diccionario_animaciones,lista_posicion_inicial[i],lista_posicion_final[i],2)
            lista_enemigos.append(enemigo)
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

class nivel_uno(Nivel):
    def __init__(self,pantalla:pygame.Surface):
        W =pantalla.get_width()
        H = pantalla.get_height()
        ##FONDO###
        fondo = pygame.image.load("platforms.png")
        fondo = pygame.transform.scale(fondo, (W,H))
        
        ##PERSONAJE###
        tamanio= (50,50)
        posicion_inicial = (H//2-200,W//2) 
        

        ##ENEMIGOS###
        lista_posicion_inicial= [(848, 510),(842,330),(590,330),(142,327)]
        lista_posicion_final=[(79,510),(590,330),(350,330),(264,327)]
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
        piso = Plataforma("piso.png",0,(0,550), 1000)
        piso_grande_uno = PlataformaDos(0,(100,370), 780,30)
        piso_grande_dos = PlataformaDos(0,(240,200),170,30)
        piso_grande_tres = PlataformaDos(0,(540,200),280,30)
        piso_grande_cuatro =PlataformaDos(0,(340,30),300,30)



        lados_piso = piso.lados# Esto devuelve un diccionario de lados que voy a recorrene en el loop para dibujarlos si yo quiero acceder solo a un lado debería poner lados_piso["bottom"] y si le agrego lados_piso["bottom"].top es la parte de arriba del bottom
        plataforma_cartel = Plataforma("plataforma_wood.png",5,(100, 300),100)
        plataforma_uno=Plataforma("plataforma_wood.png",5,(235,480),100)
        plataforma_dos = Plataforma("plataforma_wood.png",5,(234,265),100)
        plataforma_tres = Plataforma("plataforma_wood.png",5,(137,450),100)
        plataforma_cuatro = Plataforma("plataforma_wood.png",5,(783,450),100)
        plataforma_cinco = Plataforma("plataforma_wood.png",5,(688,257),100)
        plataforma_seis = Plataforma("plataforma_wood.png",5,(786,314),100)
        plataforma_siete = Plataforma("plataforma_wood.png",5,(435,130),100)
        plataforma_ocho = Plataforma("plataforma_wood.png",5,(435,80),100)
        plataforma_nueve = Plataforma("plataforma_wood.png",5,(94,407),100)
        plataforma_diez = Plataforma("plataforma_wood.png",5,(680,490),100)
        plataforma_once = Plataforma("plataforma_wood.png",5,(831,410),100)

        #Esta es la lista para las imagenes
        plataformas_clases_dos = [
                        
                        plataforma_cartel,
                        plataforma_uno,
                        plataforma_dos,
                        plataforma_tres,
                        plataforma_cuatro,
                        plataforma_cinco,
                        plataforma_seis,
                        plataforma_siete,
                        plataforma_ocho,
                        plataforma_nueve,
                        plataforma_diez,
                        plataforma_once
        ]
        #El problema ahora es que tengo que hacer lo mismo con los pisos grandes
        #Esta es la lista para los rect
        plataformas_clases = [plataforma_cartel,
                            piso_grande_cuatro,
                            piso_grande_uno,
                            piso_grande_dos,
                            piso_grande_tres,
                        plataforma_uno,
                        plataforma_dos,
                        plataforma_tres,
                        plataforma_cuatro,
                        plataforma_cinco,
                        plataforma_seis,
                        plataforma_siete,
                        plataforma_ocho,
                        plataforma_nueve,
                        plataforma_diez,
                        plataforma_once,
                        piso
                        ]
        plataformasw_1_rec = [piso.imagen, plataforma_uno.imagen, plataforma_dos.imagen,plataforma_tres.imagen]
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

        #ENEMIGOS



        plataformas_lados  = []

        item_vida = Item("vida.png", 500,2,True,False,(30,30))
        item_combustible= Item("item_combustible.png", 373,4,True,False,(30,30))
        item_weapon = Item("weapon.png",39,126,False,False,(30,30))
        lista_items = [item_combustible,item_vida, item_weapon]
        lista_vidas = []
        generar_vidas(lista_vidas,"vidas.png",lista_coordenadas,(30,30))
        lista_asteroides = []
        coordenadas_coins=[(416,14),(233,355),(294,181),(861,531),(822,352)]
        lista_coins = []
        generar_coins("coin_sprite.png",lista_coins,coordenadas_coins)
        

        #generar_vidas(lista_coins,"coin_sprite.png",coordenadas_coins,(30,30))
        jugador = Personaje ((50,50), diccionario_animaciones, posicion_inicial,10,lista_vidas)
        boss =Boss((50,50),diccionario_boss,(800,300),10,False)
        super().__init__(fondo,display,jugador,piso, plataformas_clases,plataformas_clases_dos,lista_items,lista_enemigos, lista_vidas, lista_coins,boss)
