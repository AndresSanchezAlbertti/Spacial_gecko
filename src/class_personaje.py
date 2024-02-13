import pygame
import sys
import pygame.sprite
from class_proyectil import Proyectil
from configuraciones import *
"""#atributos
    imagen
    rectangulo
    velocidad
    que_hace
    contador_pasos

    metodos:
    caminar
    saltar
"""
class Personaje(pygame.sprite.Sprite):
    def __init__(self,tamanio:tuple,animaciones, posicion_inicial:tuple,velocidad,lista_vidas):
        super().__init__()
        #self.superficie = pygame.Surface(tamanio)
        self.ancho = tamanio[0]
        self.alto = tamanio [1]
        #GRAVEDAD
        self.gravedad = 3
        #Mientraas mas grande mas fuerte cae
        self.potencia_salto = -20
        self.limite_velocidad_caida=10
        self.esta_saltando = False
        #Animaciones+
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        #self.rect.center = center
        self.reescalar_animaciones()
        self.posicion_inicial = posicion_inicial
        self.velocidad = velocidad
        
        self.listaDisparo = []
        
        #RECTANGULO
        rectangulo =self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        self.bandera_pierde =False
        self.saltos= 2
        
        #MOvimiento
        self.velocidad = velocidad
        self.desplazamiento_y= 10
        
        self.cantidad_vidas = 3
        self.lista_vidas = lista_vidas
        self.es_invulnerable = False

        self.invulnerabilidad_duracion =60
        self.invulnerabilidad_timer = 0
        self.puntaje = 0
        self.moviendose_izquierda = False
        self.intervalo_disparo = 500
        self.ultimo_disparo = 0
        self.flag_disparo = True
        self.puede_disparar = False
        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_espera = 1000
        self.direccion_proyectil = -1
        self.esta_saltando_izquierda= False
    def mover(self, velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def aplicar_gravedad(self, pantalla, piso:list):
    # Animar el salto solo al iniciar el salto
        if self.esta_saltando:
            if self.esta_saltando_izquierda:
                self.animar(pantalla, "salta_izquierda")
            
            else:
            
                self.animar(pantalla, "salta")
        
        # Aplicar la gravedad constantemente cuando esté en el aire
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
            
                self.desplazamiento_y += self.gravedad
            self.saltos-=1
    
        # Detección de colisión con el suelo
        tocando_suelo = False
        for plataforma in piso:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados["main"].top
                tocando_suelo = True
                break

        if tocando_suelo:
            self.saltos = 2  # Restablecer el contador de saltos al tocar el suelo
        else:
            self.esta_saltando = True
    def aplicar_gravedad_2(self,pantalla, piso:list):
        if self.esta_saltando and self.saltos > 0:
            
            self.saltos -=1
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
                
            
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        
        for plataforma in piso:
            if self.lados["bottom"].colliderect(plataforma.lados["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.lados["main"].top
                break
            else:
                self.esta_saltando = True
    

    def update(self,pantalla, piso,items,enemigos,lista_coins):
        self.manejo_acciones(pantalla)
        self.detectar_danio(enemigos)
        self.aplicar_gravedad(pantalla, piso)
        if not self.esta_saltando:
            self.saltos =2
    def cheq_col(self,sujeto,objeto):
        colision =False
        if sujeto.colliderect(objeto):
            colision = True
            return colision    
    def detectar_danio(self,lista_enemigos):
        i =0
        for enemigo in lista_enemigos:
            if self.cheq_col(self.lados["main"],enemigo.rectangulo):
                print (self.cantidad_vidas)
                self.respawn((100,550))
                self.morir()
                i +=1
    #def disparar(self,x,y):
     #   miProyectil = Proyectil(x,y)
      #  self.listaDisparo.append(miProyectil)
    def reescalar_animaciones (self):
        #Diccionario de animaciones
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.ancho,self.alto)
    
    def manejo_acciones(self,pantalla):
        match self.que_hace:
            case "camina_derecha":
                self.direccion_proyectil = -1
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
            case "camina_izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_izquierda")
                self.mover(self.velocidad * - 1)
            case "salta":
                if not self.esta_saltando :
                    #self.animar(pantalla,"salta")
                    self.esta_saltando_izquierda= False
                    self.esta_saltando =True
                    self.desplazamiento_y = self.potencia_salto
            case "salta_izquierda": 
                if not self.esta_saltando:
                    self.esta_saltando = False
                    self.desplazamiento_y = self.potencia_salto
                self.mover(self.velocidad * -1)
            case "quieto":
                self.direccion_proyectil = 1
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")
            case "atacando":
                if not self.esta_saltando:
                    self.animar(pantalla,"atacando")
            case "agachado":
                if not self.esta_saltando:
                    self.animar(pantalla,"agachado")
            case "muere":
                if not self.esta_saltando:
                    self.animar(pantalla, "muere")
    def animar(self, pantalla, que_animacion):
        #Tiene que ir bliteando cad a una de las imagenes de la animacion con la que voy a trabajar
        #Ante cada evento(teclass) hay que animar al personaje
        #Necesito (self,pantalla, que_animacion:str - clave del diccionario que voy a sacar del objeto que me dice que animacion hay que ejectuar)
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1
    def sumar_puntaje(self,puntaje):
        self.puntaje += puntaje
    def respawn(self,posicion_inicial):
        
        # Calcular desplazamiento
        offset_x = posicion_inicial[0] - self.rectangulo.x
        offset_y = posicion_inicial[1] 

        # Actualizar la posición principal del rectángulo
        self.rectangulo.x= posicion_inicial[0] 
        self.rectangulo.y = posicion_inicial[1] -100

        # Recalcular y actualizar los rectángulos auxiliares
        self.lados = obtener_rectangulo(self.rectangulo)
        
    
    def morir(self):
        self.que_hace= "muere"
        self.cantidad_vidas -=1

    def reescalar_animaciones (self):
        #Diccionario de animaciones
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave], self.ancho,self.alto)
    
    def disparar(self):
        # Obtener la posición inicial del disparo
        

        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.intervalo_disparo:
            # Crea un nuevo proyectil y agrégalo a la lista
            

            
            x = self.lados["right"].centerx  # Posición X del centro del personaje
            y = self.lados["right"].centery  # Posición Y del centro del personaje
            
                
            # Crear un nuevo proyectil en la posición del personaje
            
            miProyectil = Proyectil("poder_uno.png",x, y,self.direccion_proyectil)


                # Agregar el proyectil a la lista de proyectiles del personaje
            self.listaDisparo.append(miProyectil)
            self.ultimo_disparo = tiempo_actual

        
    
    
    
    
    
        