import pygame
import pygame.sprite
from modo import *
from class_enemigo import *
import sys
from class_item import *
from class_boss import *

class Nivel():
    def __init__ (self,imagen_fondo,pantalla,personaje_principal,piso, lista_plataformas,lista_platformas_dos,lista_items,lista_enemigos, lista_vidas,lista_coins,boss):
        pygame.font.init()  # Inicializa el módulo de fuentes
        self.fuente = pygame.font.Font(None, 36)
        self.fondo = imagen_fondo
        self._slave= pantalla
        self.jugador= personaje_principal
        self.plataformas = lista_plataformas
        self.plataformas_dos = lista_platformas_dos
        self.items = lista_items
        self.enemigos = lista_enemigos
        self.vidas = lista_vidas
        self.piso = piso
        
        self.coins = lista_coins
        self.boss = boss
        self.puntaje= 0
        self.tiempo_ultimo_disparo =0 
        self.flag_disparo = False
        self.tiempo_espera = 3000
        self.cantidad_enemigos = len(self.enemigos)
    def update(self,lista_eventos):
        self.actualizar_pantalla_2()
        #self.boss.actualizar(PANTALLA)
        self.colision_boss()
        self.dibujar_rectangulos()
        self.leer_inputs()
        self.get_modo(lista_eventos)

    def get_modo(self,lista_eventos):
        for evento in lista_eventos:
        
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Verificar si se hizo clic con el botón izquierdo del mouse
                    x, y = pygame.mouse.get_pos()
                    print(f"Posición del mouse - X: {x}, Y: {y}")
    def sumar_puntaje(self,puntaje):
        self.puntaje += puntaje
    def mostrar_tiempo(self, pantalla):
        
        tiempo= pygame.time.get_ticks()
        tiempo_actual = 90 - tiempo //1000   # Obtiene el tiempo en segundos
        tiempo_texto = self.fuente.render(f"Tiempo: {tiempo_actual}", True, (255,255,255))
        pantalla.blit(tiempo_texto, (10, 30))
    def obtener_tiempo(self):
        tiempo= pygame.time.get_ticks()
        tiempo_actual = 90 - tiempo //1000
        return tiempo_actual 
        
    def mostrar_puntaje(self, pantalla, puntaje):
        # Renderizar el puntaje
        texto_puntaje = self.fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))  # Blanco

        # Blitear el texto en la pantalla
        pantalla.blit(texto_puntaje, (10, 10))
    
    def dibujar_rectangulos(self):
        if get_modo ():
        #for enemigo in enemigos:
         #   for lado_enemigo in enemigo.lados:
          #      pygame.draw.rect(display, "Orange",enemigo.lados[lado_enemigo],2)        
            for lado in self.piso.lados:
                pygame.draw.rect(self._slave, "Blue", self.piso.lados[lado], 2)
            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "Orange", self.jugador.lados[lado],2)
            #for rectangulo in rectangulos_plat:
            #    pygame.draw.rect(self._slave,"Blue", rectangulo,2)
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave,"Blue", plataforma.lados[lado],2)
            for proyectil in self.jugador.listaDisparo:
                pygame.draw.rect(self._slave,"Blue", proyectil.rect,2)
            
            for item in self.items:
                if item.es_visible:
                    pygame.draw.rect(self._slave,"Blue",item.rect,2 )
            for enemigo in self.enemigos:
                    pygame.draw.rect(self._slave,"Blue",enemigo.rectangulo,2 )
            for coin in self.coins:
                pygame.draw.rect(self._slave,"Blue",coin.rect,2)
            for lado in self.boss.lados:
                if self.boss.es_visible:
                    pygame.draw.rect(self._slave, "Blue", self.boss.lados[lado],2)

    def blit_pantalla(self):
        self._slave.fill((0, 0, 0))
        self._slave.blit(self.fondo,(0,0))
    def blit_plataformas(self):
        for plataforma in self.plataformas_dos:
            self._slave.blit(plataforma.imagen,(plataforma.posicion_x,plataforma.posicion_y-8))
    def sumar_tiempo_puntaje(self):
        print(self.cantidad_enemigos)
        if self.cantidad_enemigos == 0:
            self.puntaje += self.obtener_tiempo()
            self.cantidad_enemigos = -1
            
    def gestionar_items(self):
        self.colision_item()
        self.chequear_coleccion_item()
        
    def gestionar_enemigos(self):
       
        for enemigo in self.enemigos:    
            if self.cheq_col(self.jugador.lados["bottom"],enemigo.rectangulo):
                
                enemigo.matar_enemigo(self._slave,self.enemigos)
                self.cantidad_enemigos = self.cantidad_enemigos -1
            
            for disparo in self.jugador.listaDisparo:
                if self.cheq_col(disparo.rect,enemigo.rectangulo):
                    enemigo.matar_enemigo(self._slave,self.enemigos)
                    disparo.eliminar_disparo(self.jugador.listaDisparo)
                    self.cantidad_enemigos = self.cantidad_enemigos -1
                    self.sumar_puntaje(10)
                    
                elif disparo.rect.centerx >= W-100:
                    disparo.eliminar_disparo(self.jugador.listaDisparo)
            enemigo.actualizar(PANTALLA,950,self.plataformas)
        
            if enemigo.esta_muerto:  # 2000 milisegundos = 2 segundos
                enemigo.matar_enemigo(self._slave,self.enemigos)

    
    def gestionar_coins(self):
        for coin in self.coins:
            coin.animar_item(PANTALLA)
            if  self.cheq_col(self.jugador.lados["main"],coin.rect):
            
                self.sumar_puntaje(10)
                coin.eliminar_item(self.coins)
    def colision_boss(self):
        if self.boss.es_visible:
            if self.cheq_col(self.jugador.lados["main"],self.boss.lados["left"]) or self.cheq_col(self.jugador.lados["main"],self.boss.lados["right"]) or self.cheq_col(self.jugador.lados["main"],self.boss.lados["cabeza"]):
                self.jugador.cantidad_vidas -=1
                self.jugador.respawn(self.jugador.posicion_inicial)
            
            
    def cheq_col(self,sujeto,objeto):
        colision =False
        if sujeto.colliderect(objeto):
            colision = True
            return colision
    def chequear_vidas(self):
        
        if self.jugador.cantidad_vidas ==3:
            try:
                self.vidas[0].animar(self._slave)
                self.vidas[1].animar(self._slave)
                self.vidas[2].animar(self._slave)
            except IndexError:
                pass
        elif self.jugador.cantidad_vidas== 2:
            try:
                self.vidas[0].animar(self._slave)
                self.vidas[1].animar(self._slave)
            except IndexError:
                pass
        
            
            
        elif self.jugador.cantidad_vidas ==1:
            try:
                self.vidas[0].animar(self._slave)  
            except IndexError:
                pass

    def actualizar_pantalla_2 (self):    
        self.blit_pantalla()
        self.boss.actualizar(self._slave)
        self.blit_plataformas()
        self.mostrar_puntaje(PANTALLA,self.puntaje)
        self.mostrar_tiempo(PANTALLA)
        self.obtener_tiempo()
        self.sumar_tiempo_puntaje()
        self.jugador.update(self._slave, self.plataformas,self.items, self.enemigos,self.coins)
        
        
        self.chequear_vidas()
            
        for proyectil in self.jugador.listaDisparo:
            proyectil.update(PANTALLA)
        self.gestionar_items()
        self.gestionar_enemigos()
    def colision_item(self):
        for item in self.items:

            item.animar_item(PANTALLA)
            if self.cheq_col(self.jugador.lados["main"],item.rect) and item.otorga_puntaje :
                self.puntaje += 20
                
                item.quitar_puntaje()
                item.invisibilizar(self.items)
                item.coleccionar_item()
    
    def chequear_coleccion_item(self):
        if self.items[1].coleccionado:
            self.jugador.cantidad_vidas += 1
            self.items[1].coleccionado = False
            
        if self.items[0].coleccionado:
            
            self.items[2].es_visible = True    
            if self.items[2].coleccionado:
                self.items[2].es_visible = False
                self.jugador.puede_disparar= True
        try:
            if self.items[6].coleccionado:
                self.items[5].es_visible = True
                self.items[4].es_visible =False
                self.items[3].es_visible = True 
            if self.items[4].coleccionado:
                self.items[5].es_visible=True
                self.items[4].es_visible = False
                
        except IndexError:
            pass
        
        
        
        
    
                    
       

    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and (self.jugador.lados["main"].right < ( 1000- 10)) :
            
            self.jugador.que_hace = "camina_derecha"
            self.flag_disparo=True
        elif keys[pygame.K_LEFT] and (self.jugador.lados["main"].left > 10):
            self.jugador.que_hace = "camina_izquierda"
            self.flag_disparo=True
            if self.jugador.esta_saltando:
                
                self.jugador.esta_saltando_izquierda = True
      
            
        elif keys[pygame.K_DOWN]:
            self.jugador.que_hace = "agachado"
            
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
            
        elif self.jugador.puede_disparar and self.flag_disparo and keys[pygame.K_SPACE] and self.jugador.que_hace in["quieto","salta","camina_derecha","camina_izquierda"]:
            self.jugador.que_hace = "atacando"
            self.jugador.disparar()
                
        else:
            self.jugador.que_hace = "quieto"
    
    
    
    